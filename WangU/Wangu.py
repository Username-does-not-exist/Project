import math
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


class WangU(object):
    """
    start_url:http://feizhi.fengj.com/info/
    """
    def __init__(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.start_url = "http://feizhi.fengj.com/info/"
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Host": "feizhi.fengj.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": UAPool().get()
        }

    def get_proxy(self):
        """
        获取代理
        :return:
        """
        pro = IPool().get_proxy()
        proxy = {"http": "http://" + pro}
        return pro, proxy

    def get_distract_url(self, proxy, pro):
        """
        获取每一个省份的url
        :param proxy:
        :param pro:
        :return:
        """
        try:
            response = requests.get(url=self.start_url, headers=self.headers, proxies=proxy, timeout=10)
            code = response.status_code
            while True:
                if code == 200:
                    content = response.text
                    html = etree.HTML(content)
                    urls = html.xpath('//*[@class="fenlei mzd bor_top_wu xianf"]/dd/ul/li/a/@href')
                    distract_url_list = list()
                    for i in range(1, len(urls)-3):
                        print(urls[i])
                        distract_url_list.append(urls[i])
                        return distract_url_list
                else:
                    IPool().delete_proxy(pro)
                    proxy, pro = self.get_proxy()
                    self.get_distract_url(proxy, pro)

        except Exception as e:
            print(e)

    def save_url(self, distract_url, detail_url):
        self.rConn.hset("WUrls", distract_url, 1)
        self.rConn.hset("usefulUrls", detail_url, 1)

    def get_detail_url(self, distract_url, proxy, pro):
        """
        获取详情页url
        :param distract_url:
        :param proxy:
        :param pro:
        :return:
        """
        try:
            response = requests.get(url=distract_url, headers=self.headers, proxies=proxy, timeout=5)
            code = response.status_code
            if code == 200:
                content = response.text
                html = etree.HTML(content)
                urls = html.xpath('//*[@class="main_le"]/div/ul/li/a/@href')

                num = html.xpath('/html/body/div[5]/div[1]/div/span[2]/span/text()')[0]

                set(urls)
                useful_distract_url_list = list()
                try:
                    for url in urls:
                        s_url = re.findall("http://\w+.fengj.com/detail/\d+/info_\d+.html", url)[0]
                        print("---{}---".format(s_url))
                        useful_distract_url_list.append(s_url)
                    return useful_distract_url_list, num

                except:
                    pass
            else:
                IPool().delete_proxy(pro)
                pass

        except Exception as e:
            print(e)
            pass

    def run(self):
        # distract_url_list = list()
        # distract_url_list.append(distract_url)
        runtime = random.randint(40, 60)
        stoptime = random.randint(4,6)
        pro, proxy = self.get_proxy()
        distract_url_list = self.get_distract_url(proxy, pro)
        try:
            for distract_url in distract_url_list:
                print("============{}==============".format(distract_url))
                detail_url, num = self.get_detail_url(distract_url, proxy, pro)
                page = int(num) // 15
                if page >= 150:
                    page = 150
                    for i in range(2, page):
                        next_page_url = distract_url + "page{}/".format(i)
                        print("...........{}............".format(next_page_url))
                        detail_url = self.get_detail_url(next_page_url, proxy, pro)
                        self.save_url(distract_url, detail_url)
                        time.sleep(stoptime)
                else:
                    for i in range(2, page):
                        next_page_url = distract_url + "page{}/".format(i)
                        print("...........{}............".format(next_page_url))
                        detail_url = self.get_detail_url(next_page_url, proxy, pro)
                        self.save_url(distract_url, detail_url)
                        time.sleep(stoptime)
                time.sleep(runtime)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    wangu = WangU()
    wangu.run()

