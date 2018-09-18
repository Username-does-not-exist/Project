"""
获取企业url对应的xpath://*[@id="list_item"]/div[1]/div/div/div[3]/h2/a

联系方式页面url = company_url + "contactusNews.aspx"

所需数据：公司名称 联系人 公司地址 联系电话

—__author__ "username_does_not_exist
"""

import os
import json
import random
import time
import redis
import requests
from lxml import etree
from pymongo import MongoClient
from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver import ActionChains
from requests.cookies import RequestsCookieJar
import sys
sys.path.append('../')
from UserAgentPool import UAPool


class Crawl(object):

    def __init__(self):
        self.start_url = "http://www.feijiu.net/gq/s/k%b7%cf%d6%bd/"
        self.login_url = "http://www.feijiu.net/login.aspx"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        client = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)
        self.db = client.FJqg
        self.collection = self.db.qg

    def login_and_cookies(self):
        """
        处理登陆逻辑
        :return:
        """
        # 登陆
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(5)
        # 输入账号
        username = self.driver.find_element_by_xpath('//*[@id="user"]')
        ActionChains(self.driver).move_to_element(username)
        username.click()
        username.send_keys("mixiu")
        self.driver.implicitly_wait(10)
        # 输入密码
        password = self.driver.find_element_by_xpath('//*[@id="psw"]')
        ActionChains(self.driver).move_to_element(password)
        password.send_keys('fangfei930916.+')
        # 点击登陆
        login_button = self.driver.find_element_by_xpath('//*[@id="btnUSubmit"]')
        login_button.click()
        time.sleep(5)
        cookies = self.driver.get_cookies()
        with open('cookies.txt', 'w') as file:
            json.dump(cookies, file)

        for cookie in cookies:
            self.driver.add_cookie(cookie)

    def get_company_url(self, url):
        """
        获取公司详情页联系方式的url
        :param url:
        :return:
        """
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(2)
            # GY = self.driver.find_element_by_xpath('//*[@class="type"]/div/a[1]')
            # GY.click()
            QG = self.driver.find_element_by_xpath('//*[@class="type"]/div/a[1]')
            QG.click()
            self.driver.implicitly_wait(2)
            items = self.driver.find_elements_by_xpath('//*[@class="pro_lists"]/div/div/h2/a')
            next_page_url = self.driver.find_element_by_xpath('//*[@id="AspNetPager1"]/a[last()-1]').get_attribute('href')
            url_list = []
            for item in items:
                url = item.get_attribute('href')
                url_list.append(url)
            # del url_list[0]
            # company_url_list = []
            # for url in url_list:
            #     company_url = url + "/contactusNews.aspx"
            #     print(company_url)
            #     company_url_list.append(company_url)
            return url_list, next_page_url
        except Exception as e:
            print(e)
            return None, None

    def get_contact_info(self, url):
        """
        获取公司信息
        :param url:
        :param cookies:
        :return:
        """
        try:
            self.driver.get(url)
            contact_element = self.driver.find_element_by_xpath('//*[@id="nav"]/ul/li[last()-1]/a|//*[@class="nav_list"]/li[last()]/a')
            print(contact_element.text)
            if contact_element.text != "联系我们":
                contact_element = self.driver.find_element_by_xpath('//*[@id="nav"]/ul/li[last()]/a|//*[@class="nav_list"]/li[last()-1]/a')
            contact_element.click()
            # self.driver.implicitly_wait(2)
            # print(self.driver.page_source)
            contant = self.driver.find_element_by_xpath('//*[@class="contact"]').text
            print(contant)
            # print("|================================================================================================================================|")
            company_contact_info = self.driver.find_element_by_xpath('//*[@class="contact"]/div/ul/li/img|//*[@class="contact"]/div/p/img|//*[@class="contact"]/p[1]/img').get_attribute('src')
            print(company_contact_info)
            # print(items)
            # print("|================================================================================================================================|")
            # print(contact_number_info)
            # print("|================================================================================================================================|")
            items = contant.split('\n')
            if items and company_contact_info is not None:
                return items, company_contact_info
            # self.driver.back()
        except Exception as e:
            print(e)
            # self.driver.back()
            return None, None

    def parse_data(self, company_info):
        """
        对抓取到的数据进行进一步处理
        :param company_info:
        :return:
        """
        if company_info is not None:
            li = []
            for i in company_info:
                j = i.replace('\r\n', '').replace(' ', '').replace('\u3000\u3000', '').replace('\r\n\t    ', '') \
                    .replace('\t\t\t\t\t\t', '').replace('\r\n                        ', ' ') \
                    .replace('\t', '').replace('（）', '')
                if j != '':
                    li.append(j)

            items = []
            for i in li:
                j = i.split('：')
                if len(j) > 1:
                    for k in j:
                        if k != '':
                            items.append(k)
                else:
                    items.append(j[0])
            try:
                contact_index = items.index('联系人')
                address_index = items.index('公司地址')
                info_dict = dict()
                info_dict['company'] = li[0]
                info_dict['contact'] = items[contact_index + 1]
                info_dict['address'] = items[address_index + 1]
                return info_dict
            except Exception as e:
                print(e)
                pass

    def save_data(self, info_dict, contact_info_picture_url):
        """
        保存数据
        :param data:
        :param contact_info_picture_url:
        :return:
        """
        try:
            if info_dict is not None:
                company = info_dict['company']
                path = os.getcwd()
                folder = path + "\\Image_QG"
                if not os.path.exists(folder):
                    os.mkdir(folder)
                if contact_info_picture_url is not None:
                    response = requests.get(contact_info_picture_url)
                    image = Image.open(BytesIO(response.content))
                    image.save(folder + '/{}.png'.format(company))
                self.collection.insert(info_dict)
                print(info_dict)
        except Exception as e:
            print(e)
            pass

    def __del__(self):
        self.driver.close()

    def main(self):
        """
        处理抓取逻辑
        :return:
        """
        # 1.模拟登陆获取cookies保存到本地
        self.login_and_cookies()
        # 获取企业详情页的url
        comapny_url_list, next_page_url = self.get_company_url(self.start_url)
        while True:
            for url in comapny_url_list:
                try:
                    company_info, company_contact_info = self.get_contact_info(url)
                    company_dict = self.parse_data(company_info)
                    self.save_data(company_dict, company_contact_info)
                    # self.driver.back()
                    company_url_list, next_page_url = self.get_company_url(next_page_url)
                except Exception as e:
                    print(e)
                    pass
            if next_page_url is None:
                print("抓取完成")
                break
            company_url_list, next_page_url = self.get_company_url(next_page_url)


if __name__ == '__main__':
    crawl = Crawl()
    crawl.main()
