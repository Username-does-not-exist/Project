import redis
from lxml import etree
from pymongo import MongoClient
from Pool.UserAgentPool import UAPool
import requests


class HY88(object):
    def __init__(self):
        self.base_url = "http://www.huangye88.com/search.html?kw=%E5%BA%9F%E7%BA%B8&type=company&page={}/"
        self.base_refer = "http://www.huangye88.com/search.html?kw=%E5%BA%9F%E7%BA%B8&type=company&page={}/"
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    def get_url(self):
        url_list = list()
        for i in range(2, 44):
            url = self.base_url.format(i)
            url_list.append(url)
        return url_list

    def referer(self):
        refer_list = list()
        for i in range(1, 43):
            refer = self.base_refer.format(i)
            refer_list.append(refer)
        return refer_list

    def get_deta_url(self):
        header ={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "www.huangye88.com",
            "Referer": "http://www.huangye88.com/search.html?kw=%E5%A4%96%E8%B4%B8%E6%9C%8D%E9%A5%B0&type=company&page=3/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": UAPool().get(),
        }
        url = "http://www.huangye88.com/search.html?kw=%E5%BA%9F%E7%BA%B8&type=company"
        response = requests.get(url=url, headers=header)
        contant = response.text
        html = etree.HTML(contant)
        company_url_list = html.xpath('//*[@class="pro-right"]/p/a/@href')
        return company_url_list

    def get_headers(self, refer):

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "www.huangye88.com",
            "Referer": refer,
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": UAPool().get(),
        }
        return headers

    def get_company_url(self, url, headers):
        response = requests.get(url=url, headers=headers)
        contant = response.text
        html = etree.HTML(contant)
        company_url_list = html.xpath('//*[@class="pro-right"]/p/a/@href')
        return company_url_list

    def save_url(self, company_url_list):
        """
        保存详情页的url
        :param detail_url_list:
        :return:
        """
        for url in company_url_list:
            print(url)
            self.rConn.hset("url_88fz", url, 1)

    def main(self):
        # url_list = self.get_url()
        # refer_list = self.referer()
        # for (refer, url) in zip(refer_list, url_list):
        #     # try:
        #     headers = self.get_headers(refer)
        #     company_url_list = self.get_company_url(url, headers)
        #     self.save_url(company_url_list)
        #     # except Exception as e:
        #     #     print(e)
        #     #     pass
        company_url_list = self.get_deta_url()
        self.save_url(company_url_list)


if __name__ == '__main__':
    h = HY88()
    h.main()