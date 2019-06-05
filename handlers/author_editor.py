import numpy as np


def RemoveColon(string):
    return string.replace(':', '')


def author_editor_cleanup(df):
    # some authors names have a : at the end, remove that
    df['authors'] = df['authors'].astype(str).apply(RemoveColon)
    df['editors'] = df['editors'].astype(str).apply(RemoveColon)
    return df
