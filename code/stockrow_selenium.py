from selenium import webdriver
import time
import os

with open('/Users/samfunk/ds/metis/project_mcnulty/code/tickers.txt', 'r') as f:
    tickers = f.read().split('\n')

for ind, tick in enumerate(tickers):
    if '-' in tick:
        tickers[ind] = tick.replace('-', '')

metrics_urls = ['https://stockrow.com/api/companies/%s/financials.xlsx?dimension=MRQ&section=Metrics' % tick for tick in tickers]

chromedriver = '/Applications/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)

time.sleep(30)

for url in metrics_urls[404:505]:
    driver.get(url)
