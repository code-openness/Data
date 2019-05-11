from pymongo import MongoClient
import json

client = MongoClient()
database = client['crossref']
collection = database['authors']

with open('titles_with_match_in_crossreff.txt', mode='r', encoding='utf-8') as file:
    matched_titles = file.read().split('\n')

documents = list()
for i, title in enumerate(matched_titles):
    documents.append(collection.find_one({
        "$or": [
            {
                "title": title,
            },
            {
                "container-title": title,
            }
        ]
    },
        {
            "_id": 0
        }
    ))

with open('pik_titles_in_crossref/pik_in_crossref.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(documents, indent=4, sort_keys=True))
