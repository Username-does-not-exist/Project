import datetime
import time

import requests
from lxml import etree
import redis

# def construct():
#     url_list = []
#     for i in range(1, 12):
#         url = "http://www.bianbao.net/sdList_page{}.html".format(i)
#         url_list.append(url)
#     return url_list
#
#
# def get_company_url(url):
#     response = requests.get(url)
#     content = response.text
#     html = etree.HTML(content)
#     node_list = html.xpath('//*[@class="business_info"]/div/a/@href')
#     company_url_list = []
#     for node in node_list:
#         company_url_list.append(node)
#     return company_url_list
#
#
# def company_url_list():
#     url_li = construct()
#     print(url_li.__len__())
#     for url in url_li:
#         url_list = get_company_url(url)
#     return url_list


class Crawl(object):

    def __init__(self):
        rhost = "127.0.0.1"
        rport = "6379"
        self.RedisClint = redis.Redis(host=rhost, port=rport)

    def construct(self):
        url_list = []
        for i in range(5000, 6000):
            url = "http://www.bianbao.net/sdList_page{}.html".format(i)
            url_list.append(url)
        return url_list

    def get_company_url(self, url):
        try:
            response = requests.get(url, timeout=20)
            content = response.text
            html = etree.HTML(content)
            try:
                node_list = html.xpath('//*[@class="business_info"]/div/a/@href')
                if  len(node_list) > 0:
                    company_url_list = []
                    for node in node_list:
                        company_url_list.append(node)
                    return company_url_list
                return None
            except Exception as e:
                print(e)
                pass
        except Exception as e:
            print(e)
            time.sleep(100)
            print(datetime.datetime)
            print("程序暂停运行100秒")
            pass

    def save_url(self, url_List):
        for url in url_List:
            try:
                if url is not None:
                    self.RedisClint.hset("BiBaoUrl", url, 1)
            except Exception as e:
                print(e)
                pass

    def main(self):
        url_li = self.construct()
        print(url_li.__len__())
        for url in url_li:
            url_list = self.get_company_url(url)
            if url_list is not None:
                l = len(url_list)
                print("本页抓取到{}家企业官网网址".format(l))
                self.save_url(url_list)


if __name__ == '__main__':
    Spider = Crawl()
    Spider.main()
