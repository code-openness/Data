import numpy as np
import re
import pandas as pd

# shortens name: Lastname, F.S.
def shortenNames(column):
    newValues = []

    for x, string in column.iteritems():
        # checkes whether value is nan
        if (not string) or string != string:
            newValues.append(np.nan)
            continue
        end = []

        names = [name.strip() for name in string.split(';')]
        for i, name in enumerate(names):
            ns = name.split(', ')
            # ns has to have two parts: lastname, firstname
            if len(ns) == 1:
                end.append(name)
                continue
            firstname = ns[1].strip()
            lastname = ns[0].replace(',', '').strip()

            # checkes whether the value alreaddy has short parts
            if (re.search('.\.', firstname)):
                newFN = firstname.replace('-', '').strip()
                firstnames = newFN.split(' ')

                fn = ''
                for piece in firstnames:
                    if piece == '':
                        continue
                    if (re.search('.\.', piece)):
                        fn += piece
                    else:
                        # first letter of name
                        fn += piece[0] + '.'
                end.append(lastname + ', ' + fn)
            else:
                newFN = firstname.replace('-', ' ')  # .replace(' ', '')
                firstnames = newFN.split(' ')
                fn = ''
                for piece in firstnames:
                    if piece == '':
                        continue
                    if len(piece) == 1:
                        fn += piece + '.'
                    else:
                        # first letter of name
                        fn += piece[0] + '.'
                end.append(lastname + ', ' + fn)
        newValues.append(';'.join(end))
    return pd.Series(newValues)


def author_editor_cleanup(df):
    # some authors names have a : at the end, remove that
    df['authors'] = shortenNames(df['authors'])
    df['editors'] = shortenNames(df['editors'])
    return df
