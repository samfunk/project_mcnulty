import pandas as pd
import json
from pprint import pprint
import matplotlib.pyplot as plt

with open('/Users/samfunk/ds/metis/project_mcnulty/scrapy/scrapy_yahoo/spiders/yahoo_earnings.json', 'r') as f:
    data = json.load(f)

for ind, company in enumerate(data):
    key = list(company.keys())
    values = list(company.values())[0]
    if 'N/A' in values:
        data.pop(ind)

earnings_dict = {'null': ['null', 'null']}

for ind, company in enumerate(data):
    key = list(company.keys())[0]
    values = list(company.values())[0]
    for count in range(1,5):
        earnings_dict.update({'%s_%d' % (key, count): [values[10+count], values[15+count]]})

df = pd.DataFrame.from_dict(earnings_dict, orient='index')
df = df[df.index != 'null']
df.columns = ['difference', 'surprise']

print(df.info())
