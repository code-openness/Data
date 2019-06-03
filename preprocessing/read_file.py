import pandas as pd
from html import unescape
from io import StringIO


def read_file(path):
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.read()
        print(path + ' loaded')

    # unescape to fix the encoding of some chars
    data = StringIO(unescape(data))
    print('unescaped')

    # read string as csv file
    return pd.read_csv(data, encoding="utf8", sep=',')
