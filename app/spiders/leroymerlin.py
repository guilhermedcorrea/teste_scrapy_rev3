import scrapy


class LeroymerlinSpider(scrapy.Spider):
    name = "leroymerlin"
    allowed_domains = ["leroymerlin.com.br"]
    start_urls = ["https://leroymerlin.com.br"]

    def parse(self, response):
        pass
