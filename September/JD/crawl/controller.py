import redis
from pymongo import MongoClient
from selenium import webdriver
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from cfg.config import *


class Crawl(object):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.client = MongoClient(host=HOST, port=MPORT)
        self.rConn = redis.Redis(host=HOST, port=RPORT)

    def run(self):
        """
        处理主要业务逻辑
        :return:
        """
        self.driver.get(START_URL)
        search = self.driver.find_element_by_xpath('//*[@class="form"]/input')
        button = self.driver.find_element_by_xpath('//*[@class="form"]/button')
        search.clear()
        search.send_keys(KEY_WORD)
        button.click()


if __name__ == '__main__':
    crawl = Crawl()
    crawl.run()