# 
# PC-Axis spec: https://www.scb.se/globalassets/vara-tjanster/px-programmen/px-file_format_specification_2013.pdf
#

import re
from collections import OrderedDict


__version__ = "0.0.3"

def _extend_string_list(l, values):
    if isinstance(values, list):
        l.extend(values)
    else:
        l.append(values)
    return l


def metadata_split(metadata, separator=";"):
    # matches: (?:[^\"]*\"[^\"]*\")*?;
    for m in re.split(r";(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", metadata, flags=re.MULTILINE):
        yield m
    #matches = re.finditer("(.*){0}".format(separator), metadata, re.MULTILINE)
    #for m in matches:
    #    yield m.group(0)


# keywords in CAPS and first character must be alpha
_PX_KEYWORD_RE = re.compile(r"(?P<keyword>[A-Z][A-Z0-9\-]*)(\[(?P<language>.*)\])?(\s?\((?P<subkey>.*)\))?\s?=\s?(?P<value>.*)")
# TODO: lookaheads for optional quotes
_PX_VALUE_RE = re.compile(r"\"(.*?)\"")


# TODO: use DECIMALS keyword to determine float or integer datatype (defaulting to float/double)


class PxFile(object):

    def __init__(self):
        self._meta = {}
        self._data = None
        self._keys = None

    @staticmethod
    def px_parse_value(value_string):
        if len(value_string) > 0 and value_string[0] == "\"":
            values = _PX_VALUE_RE.findall(value_string)
        else:
            values = [value_string]

        if len(values) == 1:
            return values[0]
        else:
            return values

    def px_read_meta(self, meta_text):
        for line in metadata_split(meta_text):
            if line:
                # clean line
                line = line.strip()\
                        .replace("\n", "")\
                        .replace("\"\"", "")
                m = _PX_KEYWORD_RE.search(line)
                if m:
                    keyentry = m.groupdict()
                    # if only one, extraxt from array
                    keyentry["value"] = self.px_parse_value(keyentry["value"].strip())
                    language = keyentry["language"].strip() if keyentry["language"] is not None else None
                    keyword = self._meta.setdefault(keyentry["keyword"], OrderedDict()) # python >= 3.7 dict remembers insertion order but prev ones no
                    if language:
                        keyword = keyword.setdefault(language, OrderedDict())
                    subkey = keyentry["subkey"].strip('"') if keyentry["subkey"] else None
                    keyword[subkey] = keyentry["value"]
                else:
                    print('Keyword line mismatch: "{}"'.format(line))

    def px_read_data(self, data_text):
        self._keys = self._meta.get("KEYS")
        if self._keys is not None:
            self.px_read_data_with_keys(data_text)
        else:
            self.px_read_data_no_keys(data_text)

    def px_read_data_no_keys(self, data_text):
        # TODO: check DELIMITER meta because it can be comma or other in the spec
        self._data = data_text.strip()\
                              .replace("\n", " ")\
                              .replace(";", " ") \
                              .split()  # consecutive spaces treated as single sep (use regex in the future)

    def px_read_data_with_keys(self, data_text):
        # For every variable in the stub is indicated the value for the variable within
        # quotation marks, comma separated, followed by all data cells for that row
        # (no quotation marks, space separated).

        # each stub combintation comes in a line
        self._data = {}
        nkeys = len(self._keys)
        for line in data_text.replace(";", "").splitlines():
            if line:
                data_line = line.split(",")
                nested_line = self._data
                for i in range(nkeys-1):
                    nested_line = nested_line.setdefault(data_line.pop(0), {})
                nested_line.setdefault(data_line.pop(0), data_line)

    @classmethod
    def from_string(cls, px_text):
        px = PxFile()
        meta, data = px_text.split("DATA=")
        px.px_read_meta(meta)
        px.data_str = data
        # px.px_read_data(data)
        return px

    def keywords(self):
        return self._meta.keys()

    def keyword(self, key, subkey=None, language=None):
        # check non existant
        if key in self._meta:
            lang = self._lang_key(language)

            if subkey is None:
                key_val = self._meta[key][lang] if lang is None else self._meta[key][lang][None]
            else:
                key_val = self._meta[key][subkey] if lang is None else self._meta[key][lang][subkey]

            return key_val
        else:
            return None

    def language(self):
        """
        returns default language
        """
        return self.keyword("LANGUAGE")

    def languages(self):
        """
        returns available languages
        """
        langs = self.keyword("LANGUAGES")
        if langs is None:
            if self.keyword("LANGUAGE"):
                langs = [self.keyword("LANGUAGE")]
            else:
                langs = []
        return langs

    def _lang_key(self, lang):
        """
        if lang is default language, convert to None
        """
        return lang if lang is not None and lang != self.language() else None

    def variables(self, language=None):
        variables = []
        _extend_string_list(variables, self.keyword("STUB", language=language))
        _extend_string_list(variables, self.keyword("HEADING", language=language))
        return variables

    def values(self, variable, language=None):
        v = self.keyword("VALUES", subkey=variable, language=language)
        return v if isinstance(v, list) else [v]

    def codes(self, variable, language=None):
        if "CODES" in self._meta and variable in self._meta["CODES"]:
            v =  self.keyword("CODES", subkey=variable, language=language)
            return v if isinstance(v, list) else [v]
        else:
            return self.values(variable)

    def varmap(self, variable, language=None):
        return {i: value for i, value in enumerate(self.values(variable, language=language))}

    def val_counts(self):
        return [len(self.values(v)) for v in self.variables()]

    def strides(self):
        counts = self.val_counts()
        strides = []
        for i in range(len(counts)):
            stride = 1
            for c in counts[(i+1):]:
                stride *= c
            strides.append(stride)
        return strides

    def datum(self, indexes):
        if self._data is None:
            self.px_read_data(self.data_str)

        if self._keys is not None:
            return self._datum_with_keys(indexes)
        else:
            return self._datum_no_keys(indexes)

    def _datum_no_keys(self, indexes):
        strides = self.strides()
        index = 0
        for i, x in enumerate(indexes):
            index += x * strides[i]
        try:
            return float(self._data[index])
        except ValueError:
            return None

    def _datum_keyed_stub_index(self, stub_key, index):
        # Whether the text from VALUES or from CODES are used for a variable is
        # indicated by the keyword KEYS(”var”)=CODES or
        # KEYS(”var”)=VALUES. It is possible to use VALUES from one variable
        # and CODES for another in the same file.
        # Rows that only contain 0 (zeros) are excl
        key_type = self._keys[stub_key]
        if key_type == "CODES":
            return self.codes(stub_key)[index]
        elif key_type == "VALUES":
            return self.values(stub_key)[index]

    def _datum_with_keys(self, indexes):
        data_line_keys = []
        nested_data_line = self._data
        for i, k in enumerate(self._keys.keys()):
            # assume codes
            data_line_key = self._datum_keyed_stub_index(k, indexes[i])
            nested_data_line = nested_data_line.get('"{}"'.format(data_line_key))
            if nested_data_line is None:
                # defaults to 0.0 if no data line
                return 0.0
        try:
            return float(nested_data_line[indexes[-1]])
        except ValueError:
            return None


