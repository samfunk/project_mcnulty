import scrapy
import re

class YahooSpider(scrapy.Spider):
    name = "yahoo"
    #allowed_domains = 'finance.yahoo.com'
    start_urls = [
        'https://finance.yahoo.com/quote/FB/analysts?p=FB',
    ]
    def __init__(self, filename=None):
        if filename:
            with open(filename, 'r') as f:
                self.start_urls = f.readlines()

    def parse(self, response):
        table = response.css('section[data-test]').css('table')
        yield {
            re.search(r'/([A-Z].*[A-Z])/', response.url)[1]: table[2].css('td span::text').extract()
        }
