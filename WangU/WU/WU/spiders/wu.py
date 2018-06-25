# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WuSpider(CrawlSpider):
    name = 'wu'
    allowed_domains = ['fengj.com']
    start_urls = ['http://feizhi.fengj.com/info/']

    rules = (
        Rule(LinkExtractor(allow=r'http://\w+.fengj.com/detail/\d+/info_\d+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'http://feizhi.fengj.com/info/paper_\w+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        items = dict()
        items['name'] = response.xpath('/html/body/div[4]/div[1]/div[4]/div/dl[1]/dd/a/text()').extract()[0]
        items['number'] = response.xpath('/html/body/div[2]/div[2]/p/text()').extract()[0]
        items['business'] = response.xpath('/html/body/div[4]/div[1]/div[2]/div[3]/dl[6]/dd/text()').extract()[0]
        items['distract'] = response.xpath('/html/body/div[4]/div[1]/div[4]/div/dl[7]/dd/text()').extract()[0]
        print(items)

        yield items

