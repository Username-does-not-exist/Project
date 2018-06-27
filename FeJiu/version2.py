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


class FeJiu(object):
    """
    start_url:http://www.feijiu.net/FeiZhi/g1/
    """
    def __init__(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.start_url = "http://www.feijiu.net/FeiZhi/g1/"
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    def get_distract_url_list(self):
        """
        获取各个省份对应的url
        :return:
        """
        element_list = self.driver.find_elements_by_xpath('//*[@id="area"]/div[1]/span/a')
        url_list = list()
        for element in element_list:
            url = element.get_attribute('href')
            url_list.append(url)

        distract_url_list = list()

        for i in range(1, len(url_list)):
            distract_url_list.append(url_list[i])

        return distract_url_list

    def get_detail_url_list(self):
        element_list = self.driver.find_elements_by_xpath('//*[@id="list_item"]/div[1]/div/div/div[1]/h1/a')
        url_list = list()
        for element in element_list:
            url = element.get_attribute('href')
            url_list.append(url)
        return url_list

    def parse_data(self):
        """
        获取数据
        :return:
        """
        try:
            a_str = self.driver.current_url
            a = re.findall("html", a_str)[0]
            if a == "html":
                items = dict()
                items['name'] = self.driver.find_element_by_xpath('//*[@class="message_right"]/p').text
                items['number'] = self.driver.find_element_by_xpath('//*[@class="message_right"]/p/img[1]').get_attribute('src')
                items['address'] = self.driver.find_element_by_xpath('//*[@class="message_right"]/div/span[7]').text
                items['business'] = self.driver.find_element_by_xpath('//*[@class="dlh_message"]/p[3]').text

                return items

            else:
                try:
                    element = self.driver.find_element_by_xpath('//*[@id="nav"]/ul/li[9]/a')
                    if element.text == "联系我们":
                        element.click()
                        self.driver.implicitly_wait(10)
                        items = dict()
                        items['name'] = self.driver.find_element_by_xpath('//*[@class="contact"]/div/p/span').text
                        items['number'] = self.driver.find_element_by_xpath('//*[@class="contact"]/div/ul/li[1]/img').get_attribute('src')
                        items['address'] = self.driver.find_element_by_xpath('//*[@class="contact"]/div/ul/li[4]').text
                        items['business'] = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/ul/li[3]').text
                        return items
                except:
                    pass

                try:
                    element4 = self.driver.find_element_by_xpath('//*[@id="nav"]/ul/li[5]/a')
                    if element4.text == "联系我们":
                        element4.click()
                        self.driver.implicitly_wait(10)
                        items = dict()
                        items['name'] = self.driver.find_element_by_xpath('//*[@class="contact"]/div/p/span').text
                        items['number'] = self.driver.find_element_by_xpath('//*[@class="contact"]/div/ul/li[1]/img').get_attribute('src')
                        items['address'] = self.driver.find_element_by_xpath('//*[@class="contact"]/div/ul/li[4]').text
                        items['business'] = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/div[2]/ul/li[3]').text
                        return items
                except Exception as e:
                    pass
        except Exception as e:
            print(e)
            pass

    def save_data(self, items):
        try:
            db = self.conn.FeJiu
            col = db.fejiu
            col.insert(items)
            print(items)
        except Exception as e:
            print(e)
            pass

    def __del__(self):
        self.driver.close()

    def run(self):
        self.driver.get(self.start_url)
        self.driver.implicitly_wait(10)
        distract_url_list = self.get_distract_url_list()
        for distract_url in distract_url_list:
            print("------------------------------------------")
            # 获取每一个省份的数据
            self.driver.get(distract_url)
            while True:
                detail_url_list = self.get_detail_url_list()
                for url in detail_url_list:
                    self.driver.get(url)
                    items = self.parse_data()
                    self.save_data(items)
                    print("...........................................")
                # 获取获取下一页
                try:
                    next_page = self.driver.find_element_by_xpath('//*[@id="AspNetPager1"]/a[last()-1]')
                    next_ele = self.driver.find_element_by_xpath('//*[@id="AspNetPager1"]/a[last()-1]').get_attribute('disabled')
                    if next_ele == "disabled":
                        break
                    else:
                        next_page.click()
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    feJiu = FeJiu()
    feJiu.run()

