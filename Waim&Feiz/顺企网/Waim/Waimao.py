"""
项目准备
用requests抓取
两个类别的数据个一千条 共两千条
http://b2b.11467.com/search/-59168d38670d9970.htm

详情页url对应的xpath
//*[@class="companylist"]/li/div[2]/h4/a/@href
下一页url对应的url
url_list = list()

for i in range(1,21):
url = "http://b2b.11467.com/search/-5e9f7eb8-pn{}.htm".format(i)
url_list.append(url)
return url_list


信息提取 xpath
公司名称 //*[@class="boxcontent"]/table//tr[1]/td[2]
联系人	//*[@class="boxcontent"]/dl/dd[3]
联系人电话号码 //*[@class="boxcontent"]/dl/dd[4]
固定电话 //*[@class="boxcontent"]/dl/dd[2]
邮政编码 //*[@class="boxcontent"]/dl/dd[5]
传真号码 //*[@class="boxcontent"]/dl/dd[6]
公司地址 //*[@class="boxcontent"]/dl/dd[1]

"""
import sys
import time
import redis
from lxml import etree
from pymongo import MongoClient
import requests
import re
sys.path.append('../')
from Pool.ProxyPool import IPool
from Pool.UserAgentPool import UAPool


class Waim(object):

    def __init__(self):
        self.base_url = "http://b2b.11467.com/search/-59168d38670d9970.htm"
        self.headers = {
            "User-Agent": UAPool().get()
        }
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    def get_porxy(self):
        pro = IPool().get_proxy()
        proxy = {"http": "http://" + pro}
        return proxy, pro

    def get_distract_url(self, proxy, pro):
        """
        获取每一个地区的url
        :param proxy:
        :return:
        """
        try:
            response = requests.get(url=self.base_url, headers=self.headers, proxies=proxy, timeout=5)
            content = response.text
            print(response.status_code)
            html = etree.HTML(content)
            distract_list = html.xpath('//*[@class="boxcontent"]/dl/dd/a/@href')
            distract_url_list = list()
            for distract in distract_list:
                try:
                    url = "http://" + re.findall("www.11467.com/\w+/gongsi/\w+.htm", distract)[0]
                    distract_url_list.append(url)
                except:
                    pass
            return distract_url_list
        except:
            IPool().delete_proxy(pro)

    def get_detail_url(self, url, proxy):
        """
        获取详情页的url
        :param url:
        :param proxy:
        :return:
        """
        time.sleep(2)
        response = requests.get(url=url, headers=self.headers, proxies=proxy, timeout=10)
        content = response.text
        urls = re.findall("http://www.11467.com/\w+/gongsi/\w+\-\d.htm", url)
        # 判断url是否为来自next_page_url_list
        if len(urls) != 0:
            detail_url_list = list()
            data_list = re.findall("www.11467.com/\w+/co/\w+.htm", content)
            for data in data_list:
                detail_url = "http://" + data
                print(detail_url)
                detail_url_list.append(detail_url)
            return detail_url_list
        # 不是来自next_page_url_list的url,检查是否存在多个页面，有则获取其他页面的url
        else:
            detail_url_list = list()
            next_page_url_list = list()
            data_list = re.findall("www.11467.com/\w+/co/\w+.htm", content)
            pages = re.findall("www.11467.com/\w+/gongsi/\w+\-\d.htm", content)
            for page in pages:
                next_page_url = "http://" + page
                next_page_url_list.append(next_page_url)
            for data in data_list:
                detail_url = "http://" + data
                print(detail_url)
                detail_url_list.append(detail_url)
            return detail_url_list, next_page_url_list

    def parse_data(self):
        """
        数据提取
        :return:
        """

    def save_url(self, detail_url_list):
        """
        保存详情页的url
        :param detail_url_list:
        :return:
        """
        for url in detail_url_list:
            self.rConn.hset("detail_url", url, 1)

    def save_data(self, data):
        """
        保存数据
        :return:
        """

    def main(self):
        """
        处理主要逻辑
        :return:
        """
        proxy, pro = self.get_porxy()
        distract_url_list = self.get_distract_url(proxy, pro)
        if len(distract_url_list) > 0:
            for url in distract_url_list:
                print(url)
                detail_url_list, next_page_url_list = self.get_detail_url(url, proxy)
                try:
                    # 判断是否存在下一页，如果还有下一页，则继续抓取
                    if len(next_page_url_list) > 0:
                        for next_page_url in next_page_url_list:
                            detail_url_list = self.get_detail_url(next_page_url, proxy)
                            self.save_url(detail_url_list)
                except Exception as e:
                    print(e)
                    self.save_url(detail_url_list)
        else:
            IPool().delete_proxy(pro)
            self.main()


if __name__ == '__main__':
    wm = Waim()
    wm.main()



















