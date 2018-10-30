from selenium import webdriver
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from cfg.config import *
from db.Save import save_shop_info, save_shop_url


class UrlSpider(object):
    def __init__(self):
        self.start_url = START_URL
        self.driver = webdriver.Chrome()

    def get_shop_url(self):
        items = self.driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li/div/div/span/a')
        next_page_button = self.driver.find_element('//*[@class="pn-next"')
        url_list = []
        for item in items:
            url_list.append(item.get_attribute('href'))
        return url_list, next_page_button

    def save_url(self, url_list):
        if len(url_list) > 0:
            for url in url_list:
                save_shop_url(url)

    def __del__(self):
        self.driver.close()

    def run(self):
        for key in KEYS:
            self.driver.get(self.start_url)
            search = self.driver.find_element_by_xpath('//*[@id="key"]')
            search_button = self.driver.find_element_by_xpath('//*[@class="button"]')
            search.clear()
            search.send_keys(key)
            search_button.click()
            self.driver.implicitly_wait(5)
            while True:
                url_list, next_page_button = self.get_shop_url()
                self.save_url(url_list)
                if next_page_button is not None:
                    next_page_button.click()
                    self.driver.implicitly_wait(5)
                break


if __name__ == '__main__':
    spider = UrlSpider()
    spider.run()