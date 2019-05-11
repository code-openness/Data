from pymongo import MongoClient
from habanero import Crossref
import re

client = MongoClient()
database = client['crossref']
collection = database['authors']

cr = Crossref()

with open('authors.csv', 'r', encoding='utf-8') as file:
    lines = file.readlines()

lines = [X.strip() for X in lines]

for i, author in enumerate(lines):
    print(i)
    try:
        # get the family name and the first letter of the given name in two seperate variables
        family_name = author.split(',')[0]
        first_letter_of_given_name = author.split(',')[1].strip()[0]
        # prepare a search string, which should be values sperated by a plus sign
        search_string = '+'.join(author.replace('.', ' ').replace(',', ' ').split())
        # query the api
        query = cr.works(**{'query': search_string})
        publications = query['message']['items']
        # the api also returns works in which the author has been referenced to, and not only the works he edited or authored
        # hence we refine the results according only to authering or editing
        refined_results = list()
        for result in publications:
            author_list = result.get('author', [])
            editor_list = result.get('editor', [])
            if 'reference' in result.keys():
                del (result['reference'])
            if any(re.search(family_name, X.get('family', ''), re.I) and re.search(first_letter_of_given_name,
                                                                                   X.get('given', ' ')[0], re.I) for X in
                   author_list):
                refined_results.append(result)
            if any(re.search(family_name, X.get('family', ''), re.I) and re.search(first_letter_of_given_name,
                                                                                   X.get('given', ' ')[0], re.I) for X in
                   editor_list):
                refined_results.append(result)
        for item in refined_results:
            try:
                collection.insert_one(item)
            except:
                continue
    except Exception as err:
        print(author, 'Nr', i, 'FAILED')
        print(err)
        with open('failed_author_names.txt', 'a', encoding='utf-8') as g:
            g.write(author + '\n')