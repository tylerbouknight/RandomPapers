import requests
import numpy as np
from datetime import datetime
import re

api_key = ''

# Work out the month and year to search
now = datetime.now()
month = now.month
day = now.day
year = now.year
lastmonth = month - 1
if lastmonth == 0:
    lastmonth = 12
    year = year - 1
pubdate = '%4d-%02d' % (year, lastmonth)

# make the request
r = requests.get('https://api.adsabs.harvard.edu/v1/search/query?q=*:*&fq=pubdate:' + pubdate + '&rows=2000&fq=bibstem:(MNRAS OR ApJ OR A%26A OR AJ)&fq=database:astronomy&fl=bibcode,title,doi', headers={'Authorization': 'Bearer:' + api_key})
out = r.json()

# choose random numbers
num_papers = out["response"]["numFound"]
choice = np.random.choice(num_papers, 3, replace=False)

# print out the info about the chosen papers
docs = out["response"]["docs"]
choice_count = 1
for i in choice:
    doc = docs[i]
    print(doc['title'][0])
    if 'doi' in doc and doc['doi']:
        match = re.search(r'arXiv\.([0-9./]+)', str(doc['doi']))
        if match:
            doi = match.group(1)
            print('https://arxiv.org/pdf/' + doi + '.pdf')
        else:
            print('arXiv DOI not found in format')
    else:
        print('DOI not available')

    print('')