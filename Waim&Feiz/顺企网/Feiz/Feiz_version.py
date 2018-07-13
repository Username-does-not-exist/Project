import sys
import time
import redis
from pymongo import MongoClient
import requests
import re
sys.path.append('../')
from Pool.ProxyPool import IPool
from Pool.UserAgentPool import UAPool


class FeiZ(object):

    def __init__(self):
        self.base_url = "http://b2b.11467.com/search/-5e9f7eb8.htm"
        self.headers = {
            "User-Agent": UAPool().get()
        }
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    def get_porxy(self):
        pro = IPool().get_proxy()
        proxy = {"http": "http://" + pro}
        return proxy, pro

    def get_page_url(self):
        url_list = list()
        for i in range(1, 21):
            url = "http://b2b.11467.com/search/-5e9f7eb8-pn{}.htm".format(i)
            url_list.append(url)
        return url_list

    def get_detail_url(self, url, proxy):
        """
        获取详情页的url
        :param url:
        :param proxy:
        :return:
        """
        time.sleep(3)
        print(url)
        response = requests.get(url=url, headers=self.headers, proxies=proxy)
        content = response.text
        urls = re.findall("//www.11467.com/\w+/co/\w+.htm", content)
        detail_url_list = list()
        for url in urls:
            detail_url = "http:" + url
            detail_url_list.append(detail_url)
        return detail_url_list

    def save_url(self, detail_url_list):
        """
        保存详情页的url
        :param detail_url_list:
        :return:
        """
        for url in detail_url_list:
            print(url)
            self.rConn.hset("detail_url_fz", url, 1)

    def main(self):
        proxy,pro = self.get_porxy()
        url_list = self.get_page_url()
        for url in url_list:
            detail_url_list = self.get_detail_url(url, proxy)
            self.save_url(detail_url_list)


if __name__ == '__main__':
    fz = FeiZ()
    fz.main()