import re
import redis
import requests
from pymongo import MongoClient
from lxml import etree
from selenium import webdriver
import time
import random

from Pool.ProxyPool import IPool
from Pool.UserAgentPool import UAPool


class FeizData(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "User-Agent": UAPool().get()
        }

    def get_porxy(self):
        pro = IPool().get_proxy()
        proxy = {"http": "http://" + pro}
        return proxy, pro

    def get_data(self):
        try:
            item = dict()
            item['company'] = self.driver.find_element_by_xpath('//*[@class="rigtop"]/p/a').text
            item['contact'] = self.driver.find_element_by_xpath('//*[@class="pro"]/li[4]/h3').text
            item['contact_number'] = self.driver.find_element_by_xpath('//*[@class="pro"]/li[5]/h3').text
            item['phone_number'] = self.driver.find_element_by_xpath('//*[@class="pro"]/li[6]/h3').text
            item['wechat'] = self.driver.find_element_by_xpath('//*[@class="pro"]/li[7]/h3').text
            item['QQ'] = self.driver.find_element_by_xpath('//*[@class="pro"]/li[8]/a[1]').text
            item['address'] = self.driver.find_element_by_xpath('//*[@class="rigtop"]/ul/li[2]/span').text
            return item
        except:
            item = dict()
            item['company'] = self.driver.find_element_by_xpath('//*[@class="gsname"]/a').text
            item['contact'] = self.driver.find_element_by_xpath('//*[@class="pro-text"]/ul[2]/li[1]').text
            item['contact_number'] = self.driver.find_element_by_xpath('//*[@class="prsontxt"]/p[2]').text
            item['phone_number'] = self.driver.find_element_by_xpath('//*[@class="addres"]/p[2]').text
            item['wechat'] = self.driver.find_element_by_xpath('//*[@class="pro-text"]/ul[2]/li[2]').text
            item['QQ'] = self.driver.find_element_by_xpath('//*[@class="pro-text"]/ul[2]/li[3]').text
            item['address'] = self.driver.find_element_by_xpath('//*[@class="addres"]/p[1]').text
            return item
        finally:
            item = dict()
            item['company'] = self.driver.find_element_by_xpath('//*[@class="around"]/div[4]/a').text
            item['contact'] = self.driver.find_element_by_xpath('//*[@class="basic-info"]//tr[1]/td[1]').text
            item['contact_number'] = self.driver.find_element_by_xpath('//*[@class="basic-info"]//tr[1]/td[1]').text
            item['phone_number'] = None
            item['wechat'] = None
            item['QQ'] = None
            item['address'] = self.driver.find_element_by_xpath('//*[@class="around"]/div[4]/br[1]').text
            return item

    def save_url(self, url):
        self.rConn.hset("re_url_wm", url, 1)

    def save_data(self, data):
        try:
            db = self.conn.SunFe2
            col = db.sun
            col.insert(data)
            count = col.count()
            print(data)
            print("<|---------------=================----------------|>")
            print("当前已抓取{}条数据".format(count))
        except Exception as e:
            print(e)

    def __del__(self):
        self.driver.close()

    def main(self):
        url_list = self.rConn.hgetall("url_88wm")
        for ur in url_list:
            url = ur.decode('utf-8')
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            data = self.get_data()
            print(data)
            # self.save_data(data)


if __name__ == '__main__':
    data = FeizData()
    data.main()