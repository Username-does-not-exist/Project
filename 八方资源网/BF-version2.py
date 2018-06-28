import random
import time
from pymongo import MongoClient
from selenium import webdriver
import requests
from lxml import etree
import sys
import logging
sys.path.append('./')
from UserAgentPool import UAPool
from ProxyPool import IPool

# 获取logger实例，如果参数为空则返回root logger
logger = logging.getLogger("BF")

# 指定logger输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

# 文件日志
file_handler = logging.FileHandler("bf.log")
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值

# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)


class Bfresources(object):

    """
    八方资源网外贸服饰商家信息抓取
    """
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 27017
        self.conn = MongoClient(host=self.host, port=self.port)
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

    def parse_data(self, url, proxy, pro):
        """
        获取数据
        :return:
        """
        if "html" not in url:
            try:
                self.driver.get(url)
                self.driver.implicitly_wait(5)
                time.sleep(3)
                content = self.driver.find_element_by_xpath('//*[@class="box-rightsidebar3"]/li').text
                data_list = content.split('：')
                items = dict()
                items['company_name'] = data_list[1].split('\n')[0].replace(' ', '')
                items['contacts'] = data_list[2].split('\n')[0].replace(' ', '')
                items['phone_number'] = data_list[3].split('\n')[0].replace(' ', '')
                items['post_number'] = data_list[4].split('\n')[0].replace(' ', '')
                items['mobile_number'] = data_list[5].split('\n')[0].replace(' ', '')
                items['address'] = data_list[6].split('\n')[0].replace(' ', '')
                items['messager'] = data_list[7].split('\n')[0].replace(' ', '')
                items['bf_tong'] = data_list[8].split('\n')[0].replace(' ', '')
                items['company_url'] = data_list[10].split('\n')[0].replace(' ', '')
                return items
            except Exception as e:
                logging.warning(e)

        else:
            try:
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
            except Exception as e:
                logging.warning(e)

    def save_data(self, items):
        """
        数据存储
        :return:
        """
        try:
            db = self.conn.BF
            col = db.bf
            col.insert(items)
            count = col.count()
            print(items)
            print("<|---------------=================----------------|>")
            print("当前已抓取{}条数据".format(count))
        except Exception as e:
            print(e)

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
            logging.debug("当前抓取网页的url为：{}".format(url))
            proxy, pro = self.get_proxy()
            items = self.parse_data(url, proxy, pro)
            time.sleep(runtime)
            logging.debug("抓取到的数据：{}".format(items))
            self.save_data(items)


if __name__ == '__main__':
    BF = Bfresources()
    BF.run()