# -*- coding: utf-8 -*-
import time

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver


class FejiuSpider(CrawlSpider):

    name = 'fejiu'
    allowed_domains = ['feijiu.net']
    start_urls = ['http://www.feijiu.net/gq/a1/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.feijiu.net/gq/\w+/'), follow=True),
        Rule(LinkExtractor(allow=r'\d+.html'), callback='parse_item', follow=False),
        # Rule(LinkExtractor(allow=r'http://\w+.feijiu.net/contactusNews.aspx'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        try:
            time.sleep(1)
            items = dict()
            items['name'] = response.xpath('//*[@class="message_right"]/p/text()').extract()
            items['number'] = response.xpath('//*[@class="message_right"]/p/img[1]/@src').extract()
            items['business'] = response.xpath('/html/body/div[4]/div/div[2]/div[1]/div[2]/p[3]/text()').extract()
            items['distract'] = response.xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/span[7]/text()').extract()
            print(items)
            yield items
            # items = dict()
            # items['name'] = response.xpath('').extract()
            # items['number'] = response.xpath('').extract()
            # items['business'] = response.xpath('').extract()
            # items['distract'] = response.xpath('').extract()
            # print(items)
            # yield items

        except:
            print("----------------------------------------------------------------------------------------")
