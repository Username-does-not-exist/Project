# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FejiuSpider(CrawlSpider):

    name = 'fejiu'
    allowed_domains = ['feijiu.net']
    start_urls = ['http://www.feijiu.net/FeiZhi/a1g1/']

    rules = (
        Rule(LinkExtractor(allow=r'contactusNews.aspx/'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'feijiu.net/'), callback='parse_item', follow=False),
        Rule(LinkExtractor(allow=r'http://www.feijiu.net/FeiZhi/\w+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = dict()
        items['name'] = response.xpath('//*[@class="contact"]/div/p/span/text()').extract()[0]
        items['number'] = response.xpath('//*[@class="contact"]/div/ul/li[1]/img/@src').extract()[0]
        items['business'] = response.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/ul/li[3]/text()').extract()[0]
        items['distract'] = response.xpath('//*[@class="contact"]/div/ul/li[4]/text()').extract()[0]
        print(items)
        yield items