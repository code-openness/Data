# SPARQL ready data
The files in this folder can be imported directly to the wikidata database.


Every file has at least the columns `id` and `label`.

In the column `id` are the local ids of the items saved, `label` contains the label that should be used when importing
to wikibase.

None of the files has `description` or `aliases` columns, empty strings should always be used instead.

The files are:

- `properties.csv` \
Contains a list of all properties used in the data set, exactly 18 properties. \
each property has an id, a label and one of three data types:
  - `string`: accepts a literal value
  - `item`: accepts a wikidata uri or ID
  - `multiple_items`: accepts multiple wikidata uris or IDS

- `items_0.csv` \
The first chunk of items, contains all base classes of the data to come. the columns are `id`, `label` and the local id of the `instance of` property.

- `items_1.csv` and `items_2.csv` \
Contains two levels of subclasses regarding the publication type. the columns are same as `items_0.csv`.

- `items_3.csv` \
Contains all of the items that inherit directly from the base classes and types:
  - `creators`: which are authors and editors
  - `keywords`
  - `publisher`
  - `journal`
  - `place`: place of publication
  - `conference`
  - `series`


- `items_4.csv` \
Contains all of the publications in the data set and all of the literal values.\
Every column (except `id` and `label`) is the id of one of the properties defined in the first `properties.csv` file). \
Values of the properties that are defined as `item` or `multiple_items` should be mapped before importing to the database.
