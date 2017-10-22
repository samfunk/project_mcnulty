from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import os
import tickerlist
import pickle

ticklist = tickerlist.make_list()

returns_urls = ['http://www.nasdaq.com/symbol/%s/historical' % tick.lower() for tick in ticklist]

chromedriver = '/Applications/chromedriver'
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(chromedriver)

time.sleep(30)

missing_urls = []

for url in returns_urls[303:404]:

    try:
        driver.set_page_load_timeout(10)
        driver.get(url)
        timeframe = '//select[@id="ddlTimeFrame"]/option[@value="18m"]'
        driver.find_element_by_xpath(timeframe).click()
        time.sleep(5)
        driver.find_element_by_id('lnkDownLoad').click()

    except:
        missing_urls.append(url)
        continue

with open('/Users/samfunk/ds/metis/project_mcnulty/code/missing_urls_303.pkl', 'wb') as f:
    pickle.dump(missing_urls, f)
