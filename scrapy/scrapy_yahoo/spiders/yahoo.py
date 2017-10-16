import scrapy

class YahooSpider(scrapy.Spider):
    name = "yahoo"
    allowed_domains = 'finance.yahoo.com'

    def __init__(self, tickers=[]):
        self.tickers = tickers
        self.urls = ['https://finance.yahoo.com/quote/%s/analysts?p=%s' % (tic, tic) for tic in self.tickers]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        table = response.css('section[data-test]').css('table').extract()
        headers = ['earnings est', 'revenue est', 'earnings hist', 'eps trend', 'eps revs', 'growth est']
        for ind, head in enumerate(headers):
            yield {head: table[ind]}
