import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get('https://www.slickcharts.com/sp500').text, 'html.parser')

ticklist = []
for i in soup.find('tbody').find_all('tr'):
    ticklist.append(i.find('input', {'type':'submit'}).get('value'))

def export_module(ticklist=ticklist):
    ticklist = [s.replace('.', '-') for s in ticklist]
    return ticklist

'''with open('/Users/samfunk/ds/metis/project_mcnulty/scrapy/scrapy_yahoo/spiders/yahoo_urls.txt', 'w') as f:
    for url in ['https://finance.yahoo.com/quote/%s/analysts?p=%s' % (tic, tic) for tic in ticklist]:
        f.write(str(url)+'\n')

with open('/Users/samfunk/ds/metis/project_mcnulty/scrapy/scrapy_yahoo/spiders/tickers.txt', 'w') as f:
    for tic in ticklist:
        f.write(str(tic)+'\n')'''
