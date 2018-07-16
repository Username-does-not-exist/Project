import redis
import requests
from pymongo import MongoClient
from lxml import etree
from selenium import webdriver
import time
import random

from Pool.ProxyPool import IPool
from Pool.UserAgentPool import UAPool


class WaimData(object):

    def __init__(self):
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
            "Host": "www.11467.com",
            "User-Agent": UAPool().get()
        }

    def get_porxy(self):
        pro = IPool().get_proxy()
        proxy = {"http": "http://" + pro}
        return proxy, pro

    def get_data(self, url, proxy):
        response = requests.get(url=url, headers=self.headers, proxies=proxy, timeout=5)
        print(response.status_code)
        if response.status_code != 200:
            pass
        else:
            page = response.text
            print(response.url)
            html = etree.HTML(page)
            item = dict()
            item['company'] = html.xpath('//*[@id="logo"]/h1/text()')[0]
            item['contact'] = html.xpath('//*[@class="boxcontent"]/dl/dd[3]/text()')[0]
            item['contact_number'] = html.xpath('//*[@class="boxcontent"]/dl/dd[4]/text()')[0]
            item['phone_number'] = html.xpath('//*[@class="boxcontent"]/dl/dd[2]/text()')[0]
            item['post_number'] = html.xpath('//*[@class="boxcontent"]/dl/dd[5]/text()')[0]
            item['fax'] = html.xpath('//*[@class="boxcontent"]/dl/dd[6]/text()')[0]
            item['address'] = html.xpath('//*[@class="boxcontent"]/table//tr[1]/td[2]/text()')[0]
            return item

    def save_data(self, data):
        try:
            db = self.conn.SunWaim
            col = db.sun
            col.insert(data)
            count = col.count()
            print(data)
            print("<|---------------=================----------------|>")
            print("当前已抓取{}条数据".format(count))
        except Exception as e:
            print(e)

    def main(self):
        url_list = self.rConn.hgetall("detail_url")
        for ur in url_list:
            proxy, pro = self.get_porxy()
            try:
                url = ur.decode('utf-8')
                data = self.get_data(url, proxy)
                self.save_data(data)
            except:
                IPool().delete_proxy(pro)
                pass


if __name__ == '__main__':
    data = WaimData()
    data.main()