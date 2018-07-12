# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FeizSpider(CrawlSpider):
    name = 'feiz'
    allowed_domains = ['11467.com']
    start_urls = ['http://b2b.11467.com/search/-5e9f7eb8.htm']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'),  follow=True),
        Rule(LinkExtractor(allow=r'Items/'),  follow=True),
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
