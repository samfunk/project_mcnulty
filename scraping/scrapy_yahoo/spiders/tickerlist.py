def make_list():
    with open('/Users/samfunk/ds/metis/project_mcnulty/code/tickers.txt', 'r') as f:
        tickers = f.read().split('\n')

    for ind, tick in enumerate(tickers):
        if '-' in tick:
            tickers[ind] = tick.replace('-', '')

    return tickers
