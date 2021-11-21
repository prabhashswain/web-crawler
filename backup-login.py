import scrapy
from ..items import AmazonItem
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
            'https://quotes.toscrape.com/login',
        ]

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response,formdata={
            'csrf_token':token,
            'username':'prabhashswain15@gmail.com',
            'password':'prabhashit'
        },callback=self.start_scrap)

    def start_scrap(self,response):
        open_in_browser(response)
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

        
        