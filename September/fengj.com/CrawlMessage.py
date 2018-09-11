import redis
import requests
from lxml import etree
from pymongo import MongoClient
import sys
sys.path.append('../')
from UserAgentPool import UAPool


class CrawlMessage(object):

    def __init__(self):
        rhost = "127.0.0.1"
        rport = "6379"
        self.RedisClint = redis.Redis(host=rhost, port=rport)
        mhost = '127.0.0.1'
        mport = 27017
        Client = MongoClient(host=mhost, port=mport)
        self.db = Client.gongqiu
        self.collection = self.db.gq

    def construct_headers(self, url):
        header = {
            "Referer": "http://linsen.fengj.com/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": UAPool().get()
        }
        return header

    def get_data(self, contact_url, header):
        response = requests.get(contact_url, headers=header)
        page = response.text
        html = etree.HTML(page)
        items = dict()
        items[''] = html.xpath('')
        items[''] = html.xpath('')
        items[''] = html.xpath('')
        items[''] = html.xpath('')
        return items

    def save_data(self, items):
        pass

    def main(self):
        url_list = self.RedisClint.hgetall('fengj_gongqiu')
        for i in url_list:
            url = i.decode("utf-8")
            contact_url = url + "/lxfs.html"
            header = self.construct_headers(url)
            items = self.get_data(contact_url, header)
            self.save_data(items)


if __name__ == '__main__':
    crawl = CrawlMessage()
    crawl.main()