import numpy as np
import regex as re


# a function to turn each doi into a complete link
def format_doi(value):
    doi_re = re.compile(r"^10.\d{4,9}/[-._;()/:A-Z0-9]+$", re.I)
    if type(value) is str:
        if 'doi.org' not in value and doi_re.match(value):
            return f"https://doi.org/{value}"
        else:
            return value
    else:
        return value


# a function to remove the value if not a valid DOI
def remove_invalid_doi(value):
    if type(value) is str:
        doi_re = re.compile(r"10.\d{4,9}/[-._;()/:A-Z0-9]+$", re.I)
        if doi_re.search(value) is None:
            return np.NaN
        else:
            return value
    else:
        return value


def doi_cleanup(df):
    # format all DOIs into links
    df['DOI'] = df['DOI'].apply(format_doi)
    # reset invalid dois to NaN
    df['DOI'] = df['DOI'].apply(remove_invalid_doi)
    print('doi processed')
    return df
