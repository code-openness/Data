# SPARQL ready data
the files in this folder can be imported directly to the wikidata database


every file has at least the columns `id` and `label`.

in the column `id` are the local ids of the items saved, `label` contains the label that should be used when importing
to wikibase

none of the files has `description` or `aliases` columns, empty strings should always be used instead.

the files are:

- `properties.csv` \
contains a list of all properties used in the data set, exactly 18 properties. \
each property has an id, a label and one of three data types:
  - `string`: accepts a literal value
  - `item`: accepts a wikidata uri or ID
  - `multiple_items`: accepts multiple wikidata uris or IDS

- `items_0` \
the first chunk of items, contains all base classes of the data to come

- `items_1` \
contains the first level of subclasses regarding the publication type

- `items_2` \
contains the second level of subclasses regarding the publication type

- `items_3` \
contains all of the items that inherit directly from the base classes and types:
  - `creators`: which are authors and editors
  - `keywords`
  - `publisher`
  - `journal`
  - `place`: place of publication
  - `conference`
  - `series`


- `items_4` \
contains all of the publications in the data set.\
every column (except `id` and `label` is the id of one of the
properties defined in the first `properties.csv` file)
