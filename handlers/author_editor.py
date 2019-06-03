import numpy as np


def RemoveColon(string):
    return string.replace(':', '')


def author_editor_cleanup(df):
    # remove last column, its empty
    df.drop(df.columns[len(df.columns) - 1], axis=1, inplace=True)
    # replace all \N with NaN (pandas like it this way)
    df.replace("\\N", np.nan, inplace=True)
    # some authors names have a : at the end, remove that
    df['authors'] = df['authors'].astype(str).apply(RemoveColon)
    df['editors'] = df['editors'].astype(str).apply(RemoveColon)
    return df
