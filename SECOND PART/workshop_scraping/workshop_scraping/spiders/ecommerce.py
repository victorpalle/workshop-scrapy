# -*- coding: utf-8 -*-
import scrapy


class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io/test-sites/e-commerce/static']
    start_urls = ['http://webscraper.io/test-sites/e-commerce/static/']

    def start_requests(self):
        yield scrapy.Request()

    def parse(self, response):
        self.logger.info('A response from %s just arrived!', response.url)
        pass
