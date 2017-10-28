from selenium import webdriver
import time
import os

with open('/Users/samfunk/ds/metis/project_mcnulty/datafiles/tickers.txt', 'r') as f:
    tickers = f.read().split('\n')

for ind, tick in enumerate(tickers):
    if '-' in tick:
        tickers[ind] = tick.replace('-', '')

'''metrics_urls = ['https://stockrow.com/api/companies/%s/financials.xlsx?dimension=MRQ&section=Metrics' % tick for tick in tickers]'''

income_urls = ['https://stockrow.com/api/companies/{}/financials.xlsx?dimension=MRQ&section=Income%20Statement'.format(tick) for tick in tickers]


chromedriver = '/Applications/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)

time.sleep(30)

for url in income_urls[404:]:
    driver.get(url)
