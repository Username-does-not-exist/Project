# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class WaimSpider(CrawlSpider):
    name = 'waim'
    allowed_domains = ['11467.com']
    start_urls = ['http://b2b.11467.com/search/-59168d38670d9970.htm']

    rules = (
        Rule(LinkExtractor(allow=r'\w+/gongsi/'), follow=True),
        Rule(LinkExtractor(allow=r'\w+/co/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        items = dict()
        items['company'] = response.xpath('//*[@class="boxcontent"]/table//tr[1]/td[2]/text()').extract()[0]
        items['contact'] = response.xpath('//*[@class="boxcontent"]/dl/dd[3]/text()').extract()[0]
        items['contact_number'] = response.xpath('//*[@class="boxcontent"]/dl/dd[4]/text()').extract()[0]
        items['number'] = response.xpath('//*[@class="boxcontent"]/dl/dd[2]/text()').extract()[0]
        items['post'] = response.xpath('//*[@class="boxcontent"]/dl/dd[5]/text()').extract()[0]
        items['fax'] = response.xpath('//*[@class="boxcontent"]/dl/dd[6]/text()').extract()[0]
        items['address'] = response.xpath('//*[@class="boxcontent"]/dl/dd[1]/text()').extract()[0]
        yield items
