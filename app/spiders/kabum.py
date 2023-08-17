import scrapy


class KabumSpider(scrapy.Spider):
    name = "kabum"
    allowed_domains = ["kabum.com.br"]
    start_urls = ["https://kabum.com.br"]

    def parse(self, response):
        pass
