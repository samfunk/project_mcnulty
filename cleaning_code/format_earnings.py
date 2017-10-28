import json
import re

def transform():
    with open('/Users/samfunk/ds/metis/project_mcnulty/code/yahoo_earnings.json', 'r') as f:
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

    earnings_dict.pop('null')

    with open('/Users/samfunk/ds/metis/project_mcnulty/code/final_earnings.json', 'w') as f:
        json.dump(earnings_dict, f)


transform()
