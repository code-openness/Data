import pandas as pd
import numpy as np
from opencage.geocoder import OpenCageGeocode


def place_cleanup(df):
    places = df['place']
    newCoordinates = []
    newTypes = []
    types = {}
    coordinates = {}
    key = '5421ee56399c49aa9336b0b42d5ff62c'  # enter your key; get key: https://opencagedata.com/dashboard
    if not key:
        print("No key given, no data will be requested from OpenCageGeocoder")
        return df

    geocoder = OpenCageGeocode(key)

    for x, string in places.iteritems():
        # checks whether value is nan
        if (not string) or string != string:
            newCoordinates.append(np.nan)
            newTypes.append(np.nan)
            continue

        place = places[x].replace('.', '').split(', ')
        newPlace = []
        newType = []
        for i, p in enumerate(place[:10]):
            query = place[i]
            if query not in types:
                results = geocoder.geocode(query, pretty='1', no_annotation='1')
                print(results)
                if results == []:
                    types[query] = ''
                    coordinates[query] = ''
                else:
                    types[query] = results[0]['components']['_type']
                    coordinates[query] = (results[0]['geometry']['lat'], results[0]['geometry']['lng'])

            if (types[query] == '') and (len(place) == 1):
                newTypes.append(np.nan)
                newCoordinates.append(np.nan)
            if types[query] in ('city', 'county', 'village', 'neighbourhood', 'state_district', 'state'):  # or... state_district
                newPlace.append(', '.join(map(str, (coordinates[query]))))
                newType.append(types[query])

        newTypes.append('; '.join(newType))
        newCoordinates.append('; '.join(newPlace))
    df['placeCoordinates'] = pd.Series(newCoordinates)
    df['placeTypes'] = pd.Series(newTypes)
    return df
