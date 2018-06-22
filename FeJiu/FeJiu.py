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
        # self.driver = webdriver.Chrome()
        self.start_url = "http://www.feijiu.net/FeiZhi/g1/"
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    def get_headers(self):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Host": "www.feijiu.net",
            "Referer": "http://www.feijiu.net/FeiZhi/g1/",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": UAPool().get()
        }
        return headers

    def get_proxy(self):
        """
        获取代理
        :return:
        """
        pro = IPool().get_proxy()
        proxy = {"http": "http://" + pro}
        return pro, proxy

    def get_distract_url(self, headers, proxy):
        """
        各地区url获取
        :param proxy:
        :return:
        """
        try:
            response = requests.get(self.start_url, proxies=proxy, headers=headers, timeout=10)
            if response.status_code == 200:
                page = response.text
                html = etree.HTML(page)
                url_list = html.xpath('//*[@id="area"]/div[1]/span/a/@href')
                distract_url_list = list()
                for i in range(1,len(url_list)):
                    url = url_list[i]
                    distract_url_list.append(url)
                return distract_url_list
            else:
                pass
        except Exception as e:
            print(e)

    def parse_detail_url(self, url, headers, proxy):
        """
        数据获取
        :param url:
        :param headers:
        :param proxy:
        :return:
        """
        try:
            response = requests.get(url=url, proxies=proxy, headers=headers, timeout=10)
            print(response.status_code)
            if response.status_code == 200:
                page = response.text
                html = etree.HTML(page)
                url_list = html.xpath('//*[@id="list_item"]/div[1]/div/div/div[1]/h1/a/@href')
                next_page_url = html.xpath('//*[@id="AspNetPager1"]/a[last()-1]/@href')[0]
                try:
                    element = html.xpath('//*[@id="AspNetPager1"]/a[last()-1]/@disabled')[0]
                    if element != "disabled":
                        element = None
                        return url_list, next_page_url, element
                    else:
                        return url_list, next_page_url, element
                except Exception as e:
                    print(e)
            else:
                pass
        except Exception as e:
            print("-----------------------------------------")

    def parse_data(self, url, headers, proxy):
        try:
            response = requests.get(url=url, headers=headers, proxies=proxy, timeout=5)
            if response.status_code == 200:
                page = response.text
                html = etree.HTML(page)
                items = dict()
                items[''] = html.xpath('')
                items[''] = html.xpath('')
                items[''] = html.xpath('')
                items[''] = html.xpath('')
                return items
            else:
                pass
        except Exception as e:
            print(e)

    def save_data(self, url):
        """
        报讯数据
        :param data:
        :return:
        """
        # try:
        #     db = self.conn.FeJiu
        #     col = db.fejiu
        #     col.insert(data)
        #     count = col.count()
        #     print(data)
        #     print("<|---------------=================----------------|>")
        #     print("当前已抓取{}条数据".format(count))
        # except Exception as e:
        #     print(e)

        self.rConn.hset("FeJuiURL", url, 1)

    # def __del__(self):
    #     self.driver.close()

    def run(self):
        """
        处理数据抓取逻辑
        :return:
        """
        runtime = random.randint(36, 60)
        headers = self.get_headers()
        pro, proxy = self.get_proxy()
        try:
            distract_url_list = self.get_distract_url(headers, proxy)

            detail_url_list = list()
            next_page_url_List = list()

            # 获取每一个省份的各个商家的详情页url
            for url in distract_url_list:
                try:
                    print("------------------------{}------------------------".format(url))
                    url_list, next_page_url, element = self.parse_detail_url(url, headers, proxy)
                    time.sleep(6)
                    for url in url_list:
                        detail_url_list.append(url)
                        print("-------------{}--------------".format(url))
                    if element == "disabled":
                        pass
                    else:
                        # 获取下一页
                        next_page_url_List.append(next_page_url)
                        while True:
                            for url in next_page_url_List:
                                try:
                                    print("``````````````````next_page``````````````````")
                                    url_list, next_page_url, element = self.parse_detail_url(url, headers, proxy)
                                    time.sleep(6)
                                    for url in url_list:
                                        detail_url_list.append(url)
                                        print("-------------{}--------------".format(url))
                                    if element == "disabled":
                                        pass
                                    next_page_url_List.append(next_page_url)
                                except Exception as e:
                                    print(e)
                            break

                except Exception as e:
                    print(e)

            for url in detail_url_list:
                # data = self.parse_data(url, headers, proxy)
                self.save_data(url)

        except Exception as e:
            print("***********{}**************".format(e))


if __name__ == '__main__':
    feJiu = FeJiu()
    feJiu.run()
