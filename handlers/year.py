import re

import numpy as np
import pandas as pd


def string_has_only_letters(input_string):
    if input_string is not np.NaN:
        return not any(char.isdigit() for char in input_string)
    else:
        return False


# function for cleaning short date format
def clean_short_date(value):
    # regex for dd/mm/yy and mm/dd/yy date format
    pattern = r"\d*\/\d*\/\d*"
    if value is not np.NaN:
        if re.search(pattern, value) is not None:
            year_digits = value[-2:]
            proper_year = 2000 + int(year_digits)
            return proper_year
        else:
            return value
    else:
        return value


def year_cleanup(df):
    df_copy = df.copy()
    # drop rows that contain status 'submitted' in column 'year'
    df_copy = df_copy[~df_copy['year'].str.contains(r'submitted', na=False, flags=re.IGNORECASE)]
    # drop row that contains 'Marburg' in column 'year'
    df_copy = df_copy[~df_copy['year'].apply(string_has_only_letters)]
    # extract numbers of entries in 'year' except for 'submitted' entries
    df_years = df_copy
    year = []
    for _, row in df_years.iterrows():
        _id = row['id']
        names = str(row['year']).split(' ')
        for name in names:
            year.append([_id, name.strip()])
    year = pd.DataFrame(year, columns=['id', 'year'])
    df_years = year[
        ~year['year'].str.contains('[A-Z]', regex=True, flags=re.I)]  # .to_csv("year", sep='\t', encoding='utf-8')
    # get list of rows with NaN in column'year'
    df_nan = df.copy().loc[df.copy()['year'].isnull()]
    df_nan = pd.DataFrame(df_nan, columns=['id', 'year'])
    # concatenate table of NaN entries in column 'year' and table with numerical entry
    df_concat = pd.concat([df_years, df_nan], ignore_index=True, sort=True)
    # join tables on id, add cleaned 'year' data to complete table
    result = pd.merge(df_copy,
                      df_concat[['id', 'year']],
                      on='id')
    # drop obsolete 'year' column
    result = result.drop(columns=['year_x'])
    # rename column
    result = result.rename(index=str, columns={"year_y": "year"})
    # replace values of '08/11/07' structure
    result['year'] = result['year'].apply(clean_short_date)

    # replace wrong values
    result.at['7923', 'year'] = 2018
    result.at['5588', 'year'] = 2012
    result.at['8244', 'year'] = 2018
    # replace wrong value of '16'
    result.at['6874', 'year'] = 2015
    # drop rows having '9.' as entry in column 'year'
    result = result.drop(index='7926')
    result = result.drop(index='7924')
    result = result.drop(index='7922')
    result = result.drop(index='7401')
    return result
