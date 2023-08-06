from itertools import product
import pxrd
import csv
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--languages', action="store_true", help='Show list of available languages')
    parser.add_argument('--language', help='Use <LANGUAGE> for dimensions and categories')
    args = parser.parse_args()

    px = pxrd.read(args.filename)

    if args.languages:
        for lang in px.languages():
            print("{} {}".format(lang, "(default)" if lang == px.language() else ""))
        if not px.languages():
            print('No languages defined in "{}"'.format(args.filename))
        exit(0)

    language = args.language
    if language is not None and language not in px.languages():
        print('Language "{}" not available in {}'.format(language, px.languages()))
        exit(-1)
    variables = px.variables(language=language)
    varmaps = []
    for variable in variables:
        varmaps.append(px.varmap(variable, language=language))

    heading = variables + ["value"]

    cw = csv.writer(sys.stdout)
    cw.writerow(heading)

    for index in product(*[range(v) for v in px.val_counts()]):
        index_categories = [varmaps[i][j] for i, j in enumerate(index)]
        cw.writerow(index_categories + [px.datum(index)])


if __name__ == "__main__":
    main()