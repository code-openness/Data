from pymongo import MongoClient


client = MongoClient()
database = client['crossref']
collection = database['authors']

all_titles = collection.find({}, {'title': 1, 'container-title': 1, '_id': 0})

found = []

for i, one in enumerate(all_titles):
    print(i)
    title = one.get('title', [])
    container_title = one.get('container-title', [])
    found+= title + container_title

found = set(found)

with open('all_titles.txt', mode='w', encoding='utf-8') as file:
    file.write('\n'.join(found))

