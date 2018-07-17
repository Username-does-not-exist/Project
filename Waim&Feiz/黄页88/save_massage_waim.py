import redis
from selenium import webdriver
from pymongo import MongoClient
import sys

from Pool.ProxyPool import IPool
sys.path.append('./')
from Pool.UserAgentPool import UAPool
from utils

class Feiz(object):

    def __init__(self):
        self.driver = webdriver.Firefox()
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
        """
        获取数据
        :param url:
        :param proxy:
        :return:
        """
        button = self.driver.find_element_by_xpath('//*[@class="meun"]/a[last()]|//*[@class="navigation"]/ul/li[last()]')
        button.click()
        self.driver.implicitly_wait(5)
        data_list = self.driver.find_elements_by_xpath('//*[@class="site"]/ul|//*[@class="contact-text"]')
        massage = list()
        for data in data_list:
            item = data.text
            massage.append(item)

        items = dict()
        items['company'] =





    def main(self):
        urls = self.rConn.hgetall('company_url_88fz')
        for i in urls:
            url = i.decode('utf-8')
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            data = self.get_data()
            print(data)


if __name__ == '__main__':
    f = Feiz()
    f.main()



