import scrapy
from ..items import AmazonItem


class QuotesSpider(scrapy.Spider):
    name = "amazon"

    start_urls = [
            'https://www.amazon.in/s?bbn=1389401031&rh=n%3A1389401031%2Cp_89%3ARedmi&dc&qid=1637489100&rnid=3837712031&ref=lp_1389401031_nr_p_89_3'
        ]

    def parse(self, response):
        item = AmazonItem()

        name = response.css('..a-color-base.a-text-normal').css('::text').extract()
        price = response.css('.a-price-whole').css('::text').extract()
        image = response.css('.s-image::attr(src)').extract()

        item['name'] = name
        item['price'] = price
        item['image'] = image

        yield item


        
        