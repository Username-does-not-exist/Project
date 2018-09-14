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
        self.start_url = "http://www.feijiu.net/gq/s/g1p{}k%b7%cf%d6%bd/"
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
        self.db = client.FJgy
        self.collection = self.db.gy

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
        self.driver.implicitly_wait(5)
        cookies = self.driver.get_cookies()
        with open('cookies.txt', 'w') as file:
            json.dump(cookies, file)

    def construct_url(self):
        url_list = []
        for i in range(1, 20):
            url = self.start_url.format(i)
            url_list.append(url)
        return url_list

    def get_company_url(self, url):
        """
        获取公司详情页联系方式的url
        :param url:
        :return:
        """
        try:
            session = requests.session()
            session.verify = False
            session.headers = {
                "User-Agent": UAPool().get()
            }
            # session.headers = {
            #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            #     "Accept-Encoding": "gzip, deflate",
            #     "Accept-Language": "zh-CN,zh;q=0.9",
            #     "Connection": "keep-alive",
            #     "Host": "ouyanglingfeng.feijiu.net",
            #     "Referer": "http://ouyanglingfeng.feijiu.net/",
            #     "Upgrade-Insecure-Requests": "1",
            #     "User-Agent": UAPool().get()
            # }
            jar = RequestsCookieJar()
            with open('cookies.txt', 'r') as file:
                cookies = json.load(file)
                for cookie in cookies:
                    jar.set(cookie['name'], cookie['value'])
            # proxies = {
            #     "http": "http://" + IPool().get_proxy(),
            # }
            # response = session.get(url, cookies=jar, proxies=proxies, timeout=10)
            response = session.get(url, cookies=jar)
            content = response.text
            html = etree.HTML(content)
            company_url_list = list()
            url_list = html.xpath('//*[@class="pro_lists"]/div/div/h2/a/@href')
            del url_list[0]
            for url in url_list:
                company_url = url + "/contactusNews.aspx"
                print(company_url)
                company_url_list.append(company_url)
            return company_url_list
        except Exception as e:
            print(e)
            pass

    def get_contact_info(self, url):
        """
        获取公司信息
        :param url:
        :param cookies:
        :return:
        """
        session = requests.session()
        session.verify = False
        # session.headers = {
        #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
        # }
        # session.headers = {
        #         "User-Agent": UAPool().get()
        # }
        items = url.split('/')
        del items[3]
        host = items[2]
        items[1] = "//"
        refer = items[0] + items[1] + items[2]

        session.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": host,
            "Referer": refer,
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": UAPool().get()
        }

        jar = RequestsCookieJar()
        with open('cookies.txt', 'r') as file:
            cookies = json.load(file)
            for cookie in cookies:
                jar.set(cookie['name'], cookie['value'])

        # proxies = {
        #     "http": "http://" + IPool().get_proxy(),
        # }

        # response = session.get(url, cookies=jar, proxies=proxies)
        response = session.get(url, cookies=jar)
        page = response.text
        # print("-------------------------------------------------------------------------")
        # print(page)
        html = etree.HTML(page)
        company_info = html.xpath('//*[@class="contact"]//text()')
        contact_info_picture_url = html.xpath('//*[@class="contact"]/div/ul/li/img/@src|//*[@class="contact"]/div/p/img/@src')
        # print("-------------------------------------------------------------------------")
        # print(items, '\n', contact_info_picture_url)
        # print("-------------------------------------------------------------------------")
        return company_info, contact_info_picture_url

    def parse_data(self, company_info):
        """
        对抓取到的数据进行进一步处理
        :param company_info:
        :return:
        """
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
                folder = path + "\\Image_GY"
                if not os.path.exists(folder):
                    os.mkdir(folder)
                if len(contact_info_picture_url) >= 1:
                    url = contact_info_picture_url[0]
                    response = requests.get(url)
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
        # 2.构建url
        url_list = self.construct_url()
        for url in url_list:
            try:
                # 3.获取企业联系方式页面对应的url
                company_url_list = self.get_company_url(url)
                for company_url in company_url_list:
                    # 4.提取数据
                    company_info, contact_info_picture_url = self.get_contact_info(company_url)
                    info_dict = self.parse_data(company_info)
                    # 保存数据
                    self.save_data(info_dict, contact_info_picture_url)
                    sTime = random.randint(2, 8)
                    time.sleep(sTime)
                    print("程序暂停运行{}秒".format(sTime))
            except Exception as e:
                print(e)
                pass


if __name__ == '__main__':
    crawl = Crawl()
    crawl.main()