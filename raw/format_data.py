"""
this scripts fixes the encoding of some non-UTF characters that are saved with the
Numeric character reference (for example: ç was saved as &#231;)
Thankfully, the html library can unescape these characters for so we can write the
text back as UTF
"""
from html import unescape
from io import StringIO
import pandas as pd
import numpy as np


inputFile = 'data.csv'
outputFile = 'data_formatted.csv'

data = None
with open(inputFile, 'r', encoding='UTF-8') as file:
    data = file.read()
    print(inputFile + ' loaded')

# unescape to fix the encoding of some chars
data = StringIO(unescape(data))
print('unescaped')

#read string as csv file
df = pd.read_csv(data, encoding="utf8", sep=',')

#remove last column, its empty
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)

#replace all \N with NaN (pandas like it this way)
df.replace("\\N", np.nan, inplace=True)

#some authors and editors names have a : at the end, remove that
def RemoveColon(string):
    return string.replace(':', '')

df['authors'] = df['authors'].astype(str).apply(RemoveColon)
df['editors'] = df['editors'].astype(str).apply(RemoveColon)


"""
as per Email from PIK:
Das was unter "keywords" steht sind die
alten Abteilungsnamen, die bis vor der Evaluation des Instituts in den 2000ern Bestand
hatten. Danach wurden neue Domainnamen gebildet - die ab diesem Zeitpunkt im Feld x9
hinterlegt sind. Tats?chliche Keywords liegen also, wenn vorhanden, in Feld "x1". 

however, the field x9 does not exist in the data we received
"""
df.rename(columns={
'keywords': 'oldDepartmentNames',
'x1 ( =Feld "Keyword";  u.a. belegt mit Info zu peer-review, wenn kein ISI-Journal)':'keywordsAndPeerReview',
'x4 ( = DOI / Identifier)':'DOI',
'relation (= Serie)': 'series'
}, inplace=True)



print("formatted")
df.to_csv(outputFile, encoding="utf8")

print(outputFile, "saved")

