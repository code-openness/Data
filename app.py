from handlers.author_editor import author_editor_cleanup
from handlers.place import place_cleanup
from handlers.year import year_cleanup
from preprocessing.format_data import format_data
from preprocessing.read_file import read_file
from handlers.doi import doi_cleanup
from utils.apply_cleanup import apply_cleanup

# pik_df = read_file('pik_input.csv')
pik_df = read_file('pik_refined.csv')

# import functions, and add them to the list FUNCTIONS
FUNCTIONS = [
    # format_data,  # the data was formatted, then manually cleaned with OpenRefine
    doi_cleanup,
    author_editor_cleanup,
    year_cleanup,
    place_cleanup
]

apply_cleanup(pik_df, FUNCTIONS).to_csv('pik_output.csv', index=False)
