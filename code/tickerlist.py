def make_list():
    with open('/Users/samfunk/ds/metis/project_mcnulty/code/tickers.txt', 'r') as f:
        tickers = f.read().split('\n')

    for ind, tick in enumerate(tickers):
        if '-' in tick:
            tickers[ind] = tick.replace('-', '')

    tickers.remove('GOOG')
    tickers.remove('FOXA')
    tickers.remove('DXC')
    tickers.remove('BHGE')
    tickers.remove('FTI')
    tickers.remove('BHF')
    tickers.remove('DISCK')
    tickers.remove('UAA')
    tickers.remove('NWS')
    tickers.remove('IVZ')
    tickers.pop()

    return tickers
