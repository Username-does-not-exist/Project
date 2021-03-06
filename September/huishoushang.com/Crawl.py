"""
回收商网商家信息抓取
__author__ = username does not exist

共有100个页面 每个页面20条数据 共2000条数据
"""
import re
import time
import redis
import requests
from lxml import etree
from pymongo import MongoClient
from selenium.webdriver import ActionChains
from selenium import webdriver


class Crawl(object):

    def __init__(self):
        self.start_url = "http://www.huishoushang.com/so-0-0-0-0-0-{}-0-%E5%BA%9F%E7%BA%B8.html"
        self.login_url = "http://u.huishoushang.com/Users/Login?hurl=/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        Client = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)
        self.db = Client.HSSW
        self.collection = self.db.hs

    def construct_url(self):
        url_list = []
        for i in range(1, 101):
            url = self.start_url.format(i)
            url_list.append(url)
        return url_list

    def get_information(self, url):
        response = requests.get(url)
        page = response.text
        print(response.status_code)
        html = etree.HTML(page)
        available_list = ['钻石', '银钻', '财付通', "钻石VIP"]
        contact_info_url_list = []
        level_list = html.xpath('//*[@class="userlevel_min"]//text()')
        for level in level_list:
            if level in available_list:
                info_url_list = html.xpath('//*[@class="ask_price"]/dt/a/@href')
                for info_url in info_url_list:
                    contact_info_url_list.append(info_url)
                    set(contact_info_url_list)
            return contact_info_url_list

    def get_data(self):
        """
        公司联系信息xpath: //*[@class="mt10"]/li/text()
        :param info_url:
        :return:
        """
        item = dict()
        # parser_company = re.compile(u'', re.S)
        # parser_contact = re.compile(u'', re.S)
        # parser_mobile = re.compile(u'', re.S)
        # parser_address = re.compile(u'', re.S)
        #
        # item['company'] = re.findall(parser_company, source)
        # item['contact'] = re.findall(parser_contact, source)
        # item['mobile'] = re.findall(parser_mobile, source)
        # item['address'] = re.findall(parser_address, source)
        # info = self.driver.find_element_by_xpath('')
        try:
            item['company'] = self.driver.find_element_by_xpath('//*[@class="lx_box"]|//*[@class="ablx"]|//*[@cclass="sub_us"]|//*[@cclass="contact"]').text
        except Exception as e:
            print(e)
            pass
        # item['contact'] =
        # item['mobile'] =
        # item['address'] =

        return item

    def save_data(self, data):
        try:
            self.collection.insert(data)
            print(data)
        except Exception as e:
            print(e)
            pass

    def main(self):
        # 登陆
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(5)
        # 输入账号
        username = self.driver.find_element_by_xpath('//*[@id="txt_uname"]')
        ActionChains(self.driver).move_to_element(username)
        username.click()
        username.send_keys("zhuzhu1991")
        self.driver.implicitly_wait(10)
        # 输入密码
        password = self.driver.find_element_by_xpath('//*[@id="txt_pass"]')
        ActionChains(self.driver).move_to_element(password)
        password.send_keys('zhu741852')
        # 点击登陆
        login_button = self.driver.find_element_by_xpath('//*[@id="btn1"]')
        login_button.click()
        self.driver.implicitly_wait(5)
        time.sleep(5)
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 获取url
        url_list = self.construct_url()
        for url in url_list:
            print(url)
            contact_info_url_list = self.get_information(url)
            for i in contact_info_url_list:
                info_url = i + "/Contact.html"
                self.driver.get(info_url)
                self.driver.implicitly_wait(3)
                # data = self.get_data()
                # print(data)
                # # self.save_data(data)


if __name__ == '__main__':
    crawl = Crawl()
    crawl.main()