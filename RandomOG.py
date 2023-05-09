import requests
import numpy as np
from datetime import datetime

api_key =

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
r = requests.get('https://api.adsabs.harvard.edu/v1/search/query?q=*:*&fq=pubdate:' + pubdate + '&rows=2000&fq=bibstem:(MNRAS OR ApJ OR A%26A OR AJ)&fq=database:astronomy&fl=bibcode,title', headers={'Authorization': 'Bearer:' + api_key})
out = r.json()

# choose random numbers
num_papers = out["response"]["numFound"]
choice = np.random.choice(num_papers, 3, replace=False)

# print out the info about the chosen papers
docs = out["response"]["docs"]
choice_count = 1
for i in choice:
    doc = docs[i]
    print(str(choice_count) + '. ' + doc['title'][0])
    print('   http://ui.adsabs.harvard.edu/abs/' + doc['bibcode'])
    choice_count += 1
