import re
import time
import random
import redis
import requests
from lxml import etree
from selenium import webdriver
from pymongo import MongoClient
from Pool.ProxyPool import IPool
from Pool.UserAgentPool import UAPool


class WangU(object):
    """
    start_url:http://feizhi.fengj.com/info/
    """
    def __init__(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.start_url = "http://feizhi.fengj.com/info/"
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    def get_distract_url(self):
        a_list = self.driver.find_elements_by_xpath('//*[@class="fenlei mzd bor_top_wu xianf"]/dd/ul/li/a')
        url_list = list()
        distract_url_list = list()
        for a in a_list:
            url = a.get_attribute('href')
            url_list.append(url)

        for i in range(1, len(url_list) - 3):
            print(url_list[i])
            distract_url_list.append(url_list[i])
        return distract_url_list

    def get_detail_url(self):
        b_list = self.driver.find_elements_by_xpath('//*[@class="main_le"]/div/ul/li/a')
        url_list = list()
        detail_url_list = list()
        for i in range(0,len(b_list)):
            url = b_list[i].get_attribute('href')
            url_list.append(url)

        set(url_list)
        try:
            for url in url_list:
                detail_url = re.findall('http://\w+.fengj.com/detail/\d+/info_\d+.html', url)[0]
                detail_url_list.append(detail_url)
            return detail_url_list
        except Exception as e:
            print(e)
            pass

    def save_url(self, url):
        print(url)
        self.rConn.hset('usefulurls', url, 1)

    def __del__(self):
        self.driver.close()

    def run(self):
        runtime = random.randint(40, 60)
        self.driver.get(self.start_url)
        self.driver.implicitly_wait(10)
        distract_url_list = self.get_distract_url()
        for url in distract_url_list:
            print(url)
            self.driver.get(url)
            detail_url_list = self.get_detail_url()
            self.driver.implicitly_wait(10)
            for url in detail_url_list:
                self.save_url(url)
            time.sleep(3)
            # 获取下一页
            while True:
                print("--------------------next_page----------------------")
                next_page = self.driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[16]/a[last()]').get_attribute('href')
                print(next_page)
                self.driver.get(next_page)
                print("==========================")
                self.driver.implicitly_wait(50)
                detail_url_list = self.get_detail_url()
                for url in detail_url_list:
                    self.save_url(url)
                time.sleep(runtime)


if __name__ == '__main__':
    wangu = WangU()
    wangu.run()