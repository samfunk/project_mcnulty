import json
import csv
import re

def transform(in_file, out_file):
    with open(in_file, 'r') as f:
        data = json.load(f)
    
    with open(out_file, 'w') as f:
    
        for ind, company in enumerate(data):
            key = list(company.keys())[0]
            values = list(company.values())[0]

            if 'N/A' in values:
                data.pop(ind)

            else:
                for i in range(1,5):
                    f.write('%s_%d,' % (key, 5-i))
                    f.write('%0.2f,' % float(values[10+i]))
                    f.write('%0.2f\n' % float(re.search(r'(.*)%', values[15+i].replace(',',''))[1]))
