# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FeizItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    公司名称 //*[@class="boxcontent"]/table//tr[1]/td[2]
    联系人	//*[@class="boxcontent"]/dl/dd[3]
    联系人电话号码 //*[@class="boxcontent"]/dl/dd[4]
    固定电话 //*[@class="boxcontent"]/dl/dd[2]
    邮政编码 //*[@class="boxcontent"]/dl/dd[5]
    传真号码 //*[@class="boxcontent"]/dl/dd[6]
    公司地址 //*[@class="boxcontent"]/dl/dd[1]

    """
    company = scrapy.Field()
    contact = scrapy.Field()
    contact_number = scrapy.Field()
    number = scrapy.Field()
    post = scrapy.Field()
    fax = scrapy.Field()
    address = scrapy.Field()
