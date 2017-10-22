import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
import json
import pickle

with open('/Users/samfunk/ds/metis/project_mcnulty/code/final_earnings.json', 'r') as f:
    earnings_dict = json.load(f)

df = pd.DataFrame.from_dict(earnings_dict, orient='index')
df.columns = ['difference', 'surprise']
df.rename(index={'BRK-B_1': 'BRKB_1', 'BRK-B_2': 'BRKB_2', 'BRK-B_3': 'BRKB_3', 'BRK-B_4': 'BRKB_4', 'BF-B_1': 'BFB_1', 'BF-B_2': 'BFB_2', 'BF-B_3': 'BFB_3', 'BF-B_4': 'BFB_4'}, inplace=True)

df['difference'] = df['difference'].astype(float)
def above_below(row):
    if row['difference'] < 0.0:
        return -1
    elif row['difference'] == 0.0:
        return 0
    else:
        return 1

df['above_below'] = df.apply(lambda x: above_below(x), axis=1)


df['surprise'] = df['surprise'].apply(lambda x: re.search(r'(.*)%',x)[1].replace(',', '')).astype(float)
df['abs_surprise'] = abs(df['surprise'])
df['abslog_surprise'] = df['surprise'].apply(lambda x: np.log(abs(x)))

def buckets(col, row):
    if abs(row[col]) < 5:
        return 0
    else:
        return 1

df['buckets'] = df.apply(lambda x: buckets('surprise', x), axis=1)

#sns.distplot(df.buckets)
#plt.show()

#for k,v in sorted(dict(Counter(df.surprise)).items()):
#    print('{}%: {}'.format(k,v))

with open('/Users/samfunk/ds/metis/project_mcnulty/code/earnings_df.pkl', 'wb') as f:
    pickle.dump(df, f)
