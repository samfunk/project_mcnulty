import pandas as pd
import pickle
import tickerlist

tickers = tickerlist.make_list()

dflist = []

for tick in tickers:

    with open('/Users/samfunk/ds/metis/project_mcnulty/scrapy/scrapy_yahoo/spiders/prices/%s.csv' % tick, 'r') as f:
        data = pd.read_csv(f)

    data['Date'] = pd.to_datetime(data['Date']).apply(lambda x: x.month)

    def quarters(row, tick=tick):
        if row['Date'] < 4:
            return '%s_2' % tick
        if row['Date'] > 3 and row['Date'] < 7:
            return '%s_1' % tick
        if row['Date'] > 6 and row['Date'] < 10:
            return '%s_4' % tick
        else:
            return '%s_3' % tick

    data['quarter'] = data.apply(lambda x: quarters(x), axis=1)
    data['lag'] = data['Close'].shift()
    data['return'] = data['Close'].diff() / data['lag']

    df = data[['Date', 'Close', 'quarter', 'return', 'lag']]

    df = df.groupby('quarter').agg({'return': ['mean', 'std']}).reset_index().set_index('quarter')

    dflist.append(df)

master = pd.concat(dflist)

with open('/Users/samfunk/ds/metis/project_mcnulty/scrapy/scrapy_yahoo/spiders/returns.pkl', 'wb') as f:
    pickle.dump(master, f)
