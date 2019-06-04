# PIK Data Cleanup Pipeline

This repositiory puts together the different procedures, that are being implemented to cleanup the PIK publication data.

## setup and usage

Python 3.6 or greater is needed, install the dependencies
```bash
pip install -r requirements.txt
```
the original data are in the file `pik_input.csv`, to apply the cleanup run:
```bash
python app.py
```
the cleaned data are in `pik_output.csv`. You can use the iPython `experiment_and_view.ipnyb` notebook for viewing the data the basic imports you would need for that are already on the top of the file. It would be helpful to check [this guide on Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html)

## Adding more data-cleaning blocks

You would need to write a function that takes a [pandas.Dataframe](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) object as input and returns a modified pandas.Dataframe. Include your code in a single file in the folder `handlers`. The input pandas.Datframe instance must be the output of the first handler: `preprocessing/format_data.py`. Import the new function thus in the FUNCTIONS list in `app.py`:

```python
FUNCTIONS = [
    format_data,  # this function must always run first
    doi_cleanup,
    author_editor_cleanup,
    year_cleanup,
    # YOUR ADDITIONAL FUNCTION HERE
]
```

In testing and developing the new cleanup function you can use the iPython notebook 'experiment_and_view.ipnyb', on top of which the needed preprocessed pandas.Dataframe is already imported.

## Implemented Data-Cleanup procedures:

So far, these are the inconsistencies that have been corrected:

### 0) Preprocessing

1. Ensure that cells without a value have a python [np.NaN](https://docs.scipy.org/doc/numpy-1.13.0/user/misc.html) object instead of spaces or line breaks.
2. Rename the coulmns with less ambigous names.

### 1) DOI Cleanup

1. All DOIs were turned into hyperlinks.
2. Invalid entries in the DOI coulmn were nullified.

### 2) Author and Editor Names Cleanup

remove the redundant colon ( : ) character from all the cells.

### 3) Year Cleanup
1. Entries, in which publications are marked as 'submitted', were deleted.
2. Short date forms mm/dd/yy and dd/mm/yy were converted into yyyy.
3. Some typos are corrected
