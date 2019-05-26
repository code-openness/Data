# Data

This repositiory contains all the data needed to setup the WikiData instance of PIK


## Raw data
The raw csv file can be found under `raw/data.csv`

## Manually processing the data
- Run the script `raw/format_data.py`, which would automatically create a new file name `data_formatted.csv` containing simple encoding fixes and renaming of columns
- See the `find_erroneous_data.ipynb` to check if the data has inconsistencies.
