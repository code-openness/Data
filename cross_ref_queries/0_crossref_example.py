from habanero import Crossref
import time, json

cr = Crossref()

with open('authors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

lines = [X.strip() for X in lines]

for author in lines[:5]:
    search_string = '+'.join(author.replace('.', ' ').replace(',', ' ').split())
    query = cr.works(**{'query': search_string})
    with open(f"example_results/{author}.json", 'w', encoding='utf-8') as file:
        file.write(json.dumps(query['message']['items']))
    time.sleep(1)