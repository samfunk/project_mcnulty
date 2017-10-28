import pandas as pd
from datetime import datetime
import re
import os
import tickerlist
import pickle

ticklist = tickerlist.make_list()

def format(ticker):
    with open('/Users/samfunk/ds/metis/project_mcnulty/code/metrics_csv/%s.csv' % ticker, 'r') as f:
        data = pd.read_csv(f)
        ticker = re.search(r'([A-Z]*)', os.path.basename(f.name))[1]

    data.rename(columns={'Unnamed: 0': 'quarter'}, inplace=True)
    data = data.set_index('quarter')
    data = data[data.columns[:4]]
    data = data.rename_axis(None)

    data.columns = [datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(float(date)) - 2) for date in list(data.columns)]
    data = data.transpose().reset_index()
    data.rename(columns={'index': 'date'})
    data['ticker'] = ['%s_%d' % (ticker, i) for i in range(1,len(data)+1)]

    data = data.set_index('ticker')
    data = data.rename_axis(None)

    return data


dflist = []
for ticker in ticklist:
    dflist.append(format(ticker))

metrics_df = pd.concat(dflist)

metrics_df = metrics_df.loc[:, ['index', 'Book Value per Share', 'FCF per Share', 'Interest Debt per Share', 'Cash per Share', 'Debt to Equity Ratio', 'Interest Coverage', 'Current Ratio', 'Income Quality', 'Payout Ratio', 'Intangible Assets out of Total Assets', 'Research and Development Expense of Revenue']]

metrics_df.rename(columns={'index': 'date', 'Book Value per Share': 'bookvalue', 'FCF per Share': 'fcf', 'Interest Debt per Share': 'intdebt', 'Cash per Share': 'cash', 'Debt to Equity Ratio': 'debt_equity', 'Interest Coverage': 'interest', 'Current Ratio': 'currentR'}, inplace=True)

metrics_df.rename(columns={'Income Quality': 'incomeQ', 'Payout Ratio': 'payout', 'Intangible Assets out of Total Assets': 'intangible', 'Research and Development Expense of Revenue': 'rd'}, inplace=True)

with open('/Users/samfunk/ds/metis/project_mcnulty/code/metrics.pkl', 'wb') as f:
    pickle.dump(metrics_df, f)
