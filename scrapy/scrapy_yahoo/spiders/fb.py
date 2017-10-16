import scrapy

class FBSpider(scrapy.Spider):
    name = "fb"

    start_urls = [
        'https://finance.yahoo.com/quote/FB/analysts?p=FB'
    ]


    def parse(self, response):
        table = response.css('section[data-test]').css('table').extract()
        yield {
            'earnings est': table[0],
            'revenue est': table[1],
            'earnings hist': table[2],
            'eps trend': table[3],
            'eps revs': table[4],
            'growth est': table[5]
        }

        #next_page = response.css('li.next a::attr(href)').extract_first()
        #if next_page is not None:
        #    yield response.follow(next_page, callback=self.parse)
        #    #next_page = response.urljoin(next_page)
        #    #yield scrapy.Request(next_page, callback=self.parse)
