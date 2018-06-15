import random
import time
from pymongo import MongoClient
from selenium import webdriver
import requests
from lxml import etree
import sys
sys.path.append('./')
from UserAgentPool import UAPool
from ProxyPool import IPool


class Bfresources(object):

    """
    八方资源网外贸服饰商家信息抓取
    """
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 27017
        self.conn = MongoClient(host=self.port, port=self.port)
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.b2b168.com/k-waimaofushi/l-{}.html"
        self.headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                    # "Accept-Encoding": "gzip, deflate",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "zh-CN,zh;q=0.9",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "User-Agent": UAPool().get(),
                    "Host": "www.b2b168.com"
        }

    def get_proxy(self):
        pro = IPool().get_proxy()
        proxy = {
            "http": "//" + pro
        }
        return proxy, pro

    def parse_url(self):
        """
        构造待抓取的url
        :return:
        """
        url_list = list()
        for i in range(25):
            url = self.base_url.format(i)
            url_list.append(url)
        return url_list

    def get_detail_url(self, url):
        """
        获取商家相情url
        :return:
        """
        response = requests.get(url=url)
        page = response.text
        html = etree.HTML(page)
        detail_url_list = html.xpath('//*[@id="box02"]/div/div/ul/div/h1/a/@href')
        return detail_url_list

    def parse_data(self, url, proxy):
        """
        获取数据
        :return:
        """
        if "html" not in url:
            pass
            response = requests.get(url=url, headers=self.headers, proxies=proxy)
            # if response.status_code == 200:
            #     url_list.append(response.url)
            page = response.text
            html = etree.HTML(page)
            items = dict()
            try:
                items["company_name"] = html.xpath('//*[@class="box-rightsidebar3"]/li/a[1]/text()')[0].\
                    replace(" ", "")

            except Exception as e:
                print(e)

            try:
                items["contacts"] = html.xpath('//*[@class="box-rightsidebar3"]/li/a[2]/text()')[0].\
                    replace(" ", "")
            except Exception as e:
                print(e)

            try:
                items['phone_number'] = html.xpath('//*[@class="box-rightsidebar3"]/li/text()[3]')[0].\
                    replace("\r\n\u3000\u3000电\u3000\u3000话： ", "").replace(" ", "")

            except Exception as e:
                print(e)

            try:
                items['fax'] = html.xpath('//*[@class="box-rightsidebar3"]/li/text()[4]')[0].\
                    replace("\r\n\u3000\u3000传\u3000\u3000真： ", "").replace(" ", "")
            except Exception as e:
                print(e)

            try:
                items["mobile_number"] = html.xpath('//*[@class="box-rightsidebar3"]/li/text()[5]')[0].\
                    replace("\r\n\u3000\u3000移动电话： ", "").replace(" ", "")
            except Exception as e:
                print(e)

            try:
                items['address'] = html.xpath('//*[@class="box-rightsidebar3"]/li/text()[6]')[0].\
                    replace("\r\n\u3000\u3000地\u3000\u3000址： ", "").replace(" ", "")
            except Exception as e:
                print(e)

            try:
                items['post_number'] = html.xpath('//*[@class="box-rightsidebar3"]/li/text()[7]')[0].\
                    replace("\r\n\u3000\u3000邮\u3000\u3000编： ", "").replace("\r\n\u3000\u3000\u3000\u3000邮件留言：", "").\
                    replace(" ", "")
            except Exception as e:
                print(e)

            try:
                items['messager'] = html.xpath('//*[@class="box-rightsidebar3"]/li/text()[8]')[0].\
                    replace("\r\n\u3000\u3000Messager： ", "").replace("\u3000\u3000邮件留言：", "").replace(" ", "")
            except Exception as e:
                print(e)

            try:
                items['bf_tong'] = html.xpath('//*[@class="box-rightsidebar3"]/li/text()[9]')[0].\
                    replace("\r\n\u3000\u3000八 方 通：", "").replace("\r\n\u3000\u3000Messager：", "").replace(" ", "")
            except Exception as e:
                print(e)

            try:
                items['company_url'] = html.xpath('//*[@class="box-rightsidebar3"]/li/a[5]/@href')[0].replace(" ", "")
            except Exception as e:
                print(e)
            return items
        else:
            self.driver.get(url)
            self.driver.implicitly_wait(5)
            time.sleep(3)
            items = dict()
            items["company_name"] = self.driver.find_element_by_xpath('//*[@class="Cleft"]/ul[2]').text
            items["contacts"] = self.driver.find_element_by_xpath('//*[@class="codl"]/dd[3]').text
            items["phone_number"] = self.driver.find_element_by_xpath('//*[@class="codl"]/dd[2]').text
            items["fax"] = self.driver.find_element_by_xpath('//*[@class="codl"]/dd[6]').text
            items["mobile_number"] = self.driver.find_element_by_xpath('//*[@class="codl"]/dd[4]').text
            add = self.driver.find_element_by_xpath('//*[@class="codl"]/dd[1]').text
            items["address"] = add.split(' ')[-1]
            items["post_number"] = self.driver.find_element_by_xpath('//*[@class="codl"]/dd[5]').text
            items["messager"] = ''
            items["bf_tong"] = ''
            items["company_url"] = self.driver.find_element_by_xpath('//*[@class="codl"]/dd[7]').get_attribute('href')

            if items["company_url"] == None:
                items["company_url"] = ''
            return items

    def save_data(self, items):
        """
        数据存储
        :return:
        """
        db = self.conn.BF
        col = db.bf
        col.insert(items)
        count = col.count()
        print("<|---------------=================-----------------|>")
        print("当前已抓取{}条数据".format(count))

    def run(self):
        """
        程序运行逻辑
        :return:
        """
        runtime = random.randint(1, 2)
        contact_url_list = list()
        url_list = self.parse_url()
        for url in url_list:
            detail_url_list = self.get_detail_url(url)
            for url in detail_url_list:
                if "html" in url:
                    contact_url_list.append(url)
                else:
                    contact_url = url + "contact.aspx"
                    contact_url_list.append(contact_url)

        for url in contact_url_list:
            print(url)
            proxy, pro = self.get_proxy()
            items = self.parse_data(url, proxy)
            time.sleep(runtime)
            print(items)
            self.save_data(items)


if __name__ == '__main__':
    BF = Bfresources()
    BF.run()