import redis
from pymongo import MongoClient
from selenium import webdriver
import sys
import time
import random
sys.path.append("./")


class Feiz(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.huangye88.com/"
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    def get_detail_url(self):
        items = self.driver.find_elements_by_xpath('//*[@class="wap"]/div[@class="pro-left"]/div/a')
        url_list = list()
        for item in items:
            url = item.get_attribute('href')
            url_list.append(url)
        return url_list

    def save_url(self, detail_url_list):
        """
        保存详情页的url
        :param detail_url_list:
        :return:
        """
        for url in detail_url_list:
            self.rConn.hset("url_88fz", url, 1)

    def __del__(self):
        self.driver.close()

    def main(self):
        t1 = random.randint(1, 2)
        self.driver.get(url=self.base_url)
        kw = self.driver.find_element_by_xpath('//*[@id="kw"]')
        kw.clear()
        kw.send_keys("废纸")
        time.sleep(t1)
        button = self.driver.find_element_by_xpath('//*[@id="search_btn"]')
        button.click()
        self.driver.implicitly_wait(10)
        # 获取详情页url
        detail_url_list = self.get_detail_url()
        self.save_url(detail_url_list)
        # 获取下一页数据
        t2 = random.randint(1, 3)
        while True:
            next_page = self.driver.find_element_by_xpath('//*[@class="pages"]/a[last()-1]')
            if next_page.text != "下一页":
                print(next_page.text)
                break
            else:
                next_page.click()
                self.driver.implicitly_wait(10)
                detail_url_list = self.get_detail_url()
                self.save_url(detail_url_list)
                time.sleep(t2)


if __name__ == '__main__':
    fz = Feiz()
    fz.main()