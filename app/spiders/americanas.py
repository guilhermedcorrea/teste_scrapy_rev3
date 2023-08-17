import scrapy


class AmericanasSpider(scrapy.Spider):
    name = "americanas"
    allowed_domains = ["americanas.com.br"]
    start_urls = ["https://americanas.com.br"]

    def parse(self, response):
        pass
