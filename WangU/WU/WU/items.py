# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    客户姓名、电话号码、主营业务、地区
    """

    name = scrapy.Field()
    number = scrapy.Field()
    business = scrapy.Field()
    distract = scrapy.Field()
