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
        self.db = Client.gongying
        self.collection = self.db.gy

    def construct_headers(self):
        header = {
            "Referer": "http://linsen.fengj.com/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": UAPool().get()
        }
        return header

    def get_data(self, contact_url, header):
        try:
            response = requests.get(contact_url, headers=header, timeout=10)
            page = response.text
            html = etree.HTML(page)
            items = dict()
            items['company'] = html.xpath('//*[@class="person_info"]/dl[last()-1]/dd//text()')[0]
            items['contact'] = html.xpath('//*[@class="person_info"]/dl[1]/dd//text()')[0]
            items['mobile'] = html.xpath('//*[@class="phone"]/p/text()')[0]
            items['address'] = html.xpath('//*[@class="person_info"]/dl[last()]/dd//text()')[0]
            return items
        except Exception as e:
            print(e)
            pass

    def save_data(self, items):
        try:
            self.collection.insert(items)
            print(items)
        except Exception as e:
            print(e)
            pass

    def main(self):
        url_list = self.RedisClint.hgetall('fengj_gongying')
        for i in url_list:
            url = i.decode("utf-8")
            contact_url = url + "/lxfs.html"
            header = self.construct_headers()
            items = self.get_data(contact_url, header)
            self.save_data(items)


if __name__ == '__main__':
    crawl = CrawlMessage()
    crawl.main()