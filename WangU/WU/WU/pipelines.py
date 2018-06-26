# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class WuPipeline(object):
    def process_item(self, item, spider):
        return item


class MongoPipeline(object):

    def __init__(self):
        host = settings["MONGODB_HOST"]
        port = settings["MONGODB_PORT"]
        db = settings["MONGODB_DB"]
        collection = settings["MONGODB_COLLECTION"]
        client = pymongo.MongoClient(host=host, port=port)
        # 指定数据库
        my_db = client[db]
        # 存放数据的数据库表名
        self.post = my_db[collection]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

