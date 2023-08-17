import scrapy


class GoogleshoppingSpider(scrapy.Spider):
    name = "googleshopping"
    allowed_domains = ["shopping.google.com.br"]
    start_urls = ["https://shopping.google.com.br"]

    def parse(self, response):
        pass
