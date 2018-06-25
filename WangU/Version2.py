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
        print("-----------------------------------------------------------")
        b_list = self.driver.find_elements_by_xpath('/html/body/div[7]/div[1]/div/ul/li[2]/h2/a')
        num = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div/span[2]/span').text
        url_list = list()
        detail_url_list = list()
        for i in b_list:
            url = i.get_attribute('href')
            url_list.append(url)

        set(url_list)
        try:
            for url in url_list:
                detail_url = re.findall('http://\w+.fengj.com/detail/\d+/info_\d+.html', url)[0]
                detail_url_list.append(detail_url)
            return detail_url_list, num
        except Exception as e:
            print(e)
            pass

    def save_url(self, detail_url, distract_url):
        print(detail_url)
        self.rConn.hset("WUrls", distract_url, 1)
        self.rConn.hset('usefulurls', detail_url, 1)

    def __del__(self):
        self.driver.close()

    def run(self):
        runtime = random.randint(40, 60)
        stoptime = random.randint(4, 6)
        self.driver.get(self.start_url)
        self.driver.implicitly_wait(10)
        distract_url_list = self.get_distract_url()
        for distract_url in distract_url_list:
            self.driver.get(distract_url)
            detail_url_list, num = self.get_detail_url()
            self.driver.implicitly_wait(10)
            for detail_url in detail_url_list:
                self.save_url(detail_url, distract_url)
            time.sleep(3)
            # 获取下一页
            page = int(num) // 15
            if page >= 150:
                page = 150
                for i in range(1, page):
                    try:
                        next_page_url = distract_url + "page{}/".format(i)
                        print("...........{}............".format(next_page_url))
                        self.driver.get(next_page_url)
                        self.driver.implicitly_wait(10)
                        detail_url_list, num = self.get_detail_url()
                        for detail_url in detail_url_list:
                            self.save_url(detail_url, distract_url)
                        time.sleep(stoptime)
                    except Exception as e:
                        print(e)
                        pass

            else:
                for i in range(1, page):
                    try:
                        next_page_url = distract_url + "page{}/".format(i)
                        print("...........{}............".format(next_page_url))
                        self.driver.get(next_page_url)
                        self.driver.implicitly_wait(10)
                        detail_url_list, num = self.get_detail_url()
                        for detail_url in detail_url_list:
                            self.save_url(detail_url, distract_url)
                        time.sleep(stoptime)
                    except Exception as e:
                        print(e)
                        pass
            time.sleep(runtime)


if __name__ == '__main__':
    wangu = WangU()
    wangu.run()