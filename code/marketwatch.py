import requests
from bs4 import BeautifulSoup
import re
import tickerlist
import pickle
from collections import defaultdict


ticklist = tickerlist.make_list()
ticklist = [tic.lower().replace('-', '.') for tic in ticklist]

sect_ind_dict = defaultdict(list)

for tic in ticklist:
    url = 'https://www.marketwatch.com/investing/stock/%s/profile' % tic
    print(tic)
    print(url)
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')

    ind = soup.find('div', {'class': 'twowide addgutter'}).find_all('div', {'class':'section'}) [1].find_all('p')[1].text

    sect = soup.find('div', {'class': 'twowide addgutter'}).find_all('div', {'class':'section'}) [2].find_all('p')[1].text

    print(sect)
    print(ind)

    sect_ind_dict[tic.upper()] = [sect, ind]

with open('/Users/samfunk/ds/metis/project_mcnulty/code/sector_industries.pkl', 'wb') as f:
    pickle.dump(sect_ind_dict, f)

'''class NasdaqSpider(scrapy.Spider):
    name = "nasdaq"
    #allowed_domains = 'finance.yahoo.com'

    def __init__(self, filename=None):
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = f.readlines()

    def parse(self, response):
        table = response.css('section[data-test]').css('table')
        yield {
            re.search(r'symbol/(.*)/hist', response.url)[1].upper(): response.css('span[id=qbar_sectorLabel] a::text').extract_first()
            #response.css('span[id=qbar_exchangeLabel]::text').extract_first()
        }
'''
