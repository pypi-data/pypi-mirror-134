#  Copyright 2018-2020 by Asier Murciego Alonso <asier.murciego@orkestra.deusto.es>, Basque Institute of Competitiveness
#
#  All rights reserved.
#  This file is part of the Hontza Indicator Data Warehouse
#

from itertools import count, product
import pandas as pd


def _indexed_data(px):
    for index in product(*[range(v) for v in px.val_counts()]):
        yield index + (px.datum(index),)

def to_pandas(px, categories=True, multiindex=False, language=None):
    variables = px.variables(language=language)
    cols = variables + ["DATA"]
    df = pd.DataFrame(data=_indexed_data(px), columns=cols)
    
    if categories:
        for variable in variables:
            df[variable] = df[variable].map(px.varmap(variable, language=language))

    if multiindex:
        df.set_index(keys=variables, drop=True, inplace=True)

    return df