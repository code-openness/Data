import pandas as pd
import regex
pik_data = pd.read_csv('data_formatted.csv')

pik_titles = [X for X in list(pik_data['title']) if type(X) is str]
pik_titles = [X for X in pik_titles if len(X.split()) > 2]


with open('all_titles.txt', mode='r', encoding='utf-8') as file:
    titles_from_crossref = file.read().split('\n')

titles_from_crossref = { regex.sub(r'[^\w\s]',' ', x.strip()):x  for x in titles_from_crossref}

for i, title in enumerate(pik_titles):
    print(i)
    search_string = regex.sub(r'[^\w\s]',' ', title.strip())
    expression = regex.compile(f"({search_string}){{e<=4}}", regex.IGNORECASE)
    try:
        result = next(x for x in titles_from_crossref.keys() if expression.match(x) is not None)
        print(search_string)
        print(titles_from_crossref[result])
        with open('titles_with_match_in_crossreff.txt', 'a', encoding='utf-8') as g:
            g.write(titles_from_crossref[result] + '\n')
    except StopIteration:
        continue

