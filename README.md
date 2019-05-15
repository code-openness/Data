# Data

this repositiory contains all the data needed to setup the WikiData instance of PIK


## Raw data
the raw csv file can be found under `raw/data.csv`

## Manually processing the data
- run the script `raw/format_data.py`, which would automatically create a new file name `data_formatted.csv` containing simple encoding fixes and renaming of columns
- see the `find_erroneous_data.ipynb` to check if the data has inconsistencies.