import pandas as pd
import numpy as np
from opencage.geocoder import OpenCageGeocode

def place_cleanup(df):
    places = df['place']
    newValues = []
    types = {}
    coordinates = {}
    key = ''  # enter your key; get key: https://opencagedata.com/dashboard
    geocoder = OpenCageGeocode(key)

    for x, string in places.iteritems():
        # checkes whether value is nan
        if (not string) or string != string:
            newValues.append(np.nan)
            continue

        place = places[x].replace('.', '').split(', ')
        newPlace = []
        for i, p in enumerate(place):
            query = place[i]
            if query not in types:
                results = geocoder.geocode(query, pretty='1', no_annotation='1')
                if results == []:
                    types[query] = ''
                    coordinates[query] = ''
                else:
                    types[query] = results[0]['components']['_type']
                    coordinates[query] = (results[0]['geometry']['lat'], results[0]['geometry']['lng'])

            if (types[query] == '') and (len(place) == 1):
                newValues.append(np.nan)
            if types[query] in ('city', 'county', 'village', 'neighbourhood', 'state_district', 'state'):
                newPlace.append(', '.join(map(str, (coordinates[query]))))

        newValues.append('; '.join(newPlace))
    df['place'] = pd.Series(newValues)
    return df