import scrapy
from ..items import AmazonItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_number = 1
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
        ]

    def parse(self, response):
        item = AmazonItem()

        all_div_quote = response.css('div.quote')
        
        for i in all_div_quote:
            title = i.css('span.text::text').extract()
            author = i.css('.author::text').extract()
            tag = i.css('.tag::text').extract()

            item['title'] = title
            item['author'] = author
            item['tag'] = tag

            yield item

        next_page = 'http://quotes.toscrape.com/page/' + str(QuotesSpider.page_number)  + '/'

        if QuotesSpider.page_number < 11:
            QuotesSpider.page_number += 1

            yield response.follow(next_page,callback=self.parse)
