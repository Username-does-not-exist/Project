import re
import time
import redis
from selenium import webdriver
from pymongo import MongoClient


class FeJiu(object):
    """
    start_url:http://www.feijiu.net/FeiZhi/g1/
    """
    def __init__(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    def get_url(self):
        url_dict = self.rConn.hgetall("FeJuiURL")
        url_dict2 = self.rConn.hgetall("FeJuiDisableURL")
        url_list = list()
        for item in url_dict2.keys():
            url = item.decode('utf-8')
            url_list.append(url)
        for item in url_dict.keys():
            url = item.decode('utf-8')
            url_list.append(url)
        return url_list

    def get_data(self):
        try:
            items = dict()
            items['name'] = self.driver.find_element_by_xpath('//*[@class="message_right"]/p'). \
                text.split(':')[1].replace('\n联系电话', '')

            items['number'] = self.driver.find_element_by_xpath(
                '//*[@class="message_right"]/p/img[1]').get_attribute('src')

            items['address'] = self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div[2]/div[2]/div[1]/span[7]') \
                .text.split('：')[1].replace(' ', '')

            items['business'] = self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div[2]/div[1]/div[2]/p[3]').text
            print(items)
            return items
        except:
            print("----------------------------------------------------------------")

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
        url_list = self.get_url()
        for url in url_list:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            items = self.get_data()
            self.save_data(items)


if __name__ == '__main__':
    F = FeJiu()
    F.run()