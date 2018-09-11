import re
import time

import redis
import sys
import requests
from lxml import etree

sys.path.append("../")
from UserAgentPool import UAPool


class Crawl(object):

    def __init__(self):
        rhost = "127.0.0.1"
        rport = "6379"
        self.RedisClint = redis.Redis(host=rhost, port=rport)

    def construct(self):
        url_list = []
        headers2 = []
        for i in range(2, 94):
            url = "http://www.fengj.com/so/SearchInfo.aspx?keyword=%b7%cf%d6%bd&info_type=sell&page={}".format(i)
            url_list.append(url)
            header = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Cache-Control": "max-age=0",
                "Host": "www.fengj.com",
                "Proxy-Connection": "keep-alive",
                "Referer": url,
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": UAPool().get()
            }
            headers2.append(header)

        return url_list,headers2

    def construct_headers(self):
        headers1 = []
        for i in range(1, 93):
            header = {
                "Referer": "http://www.fengj.com/so/SearchInfo.aspx?keyword=%b7%cf%d6%bd&info_type=sell&page={}".format(i),
                "Upgrade-Insecure-Requests": "1",
                "User-Agent": UAPool().get()
                }
            headers1.append(header)
        return headers1

    def get_data(self, url, header):
        response = requests.get(url=url, headers=header, timeout=10)
        content = response.text
        html = etree.HTML(content)
        node_list = html.xpath('//*[@id="liebiao"]/div[1]/div[1]/div/div[2]/span[1]/span/a/@href')
        if len(node_list) > 0:
            return node_list

    def get_company_url(self, url, header):
        response = requests.get(url=url, headers=header, timeout=10)
        time.sleep(1)
        print(response.status_code)
        content = response.text
        parser = re.compile(u"<a href='(http://\w+.fengj.com)' target='_blank' >", re.S)
        urls = re.findall(parser, content)
        return urls

    def save_url(self, urls):
        if len(urls) == 0:
            pass
        else:
            for url in urls:
                self.RedisClint.hset('fengj_gongying', url, 1)
                print(url)

    def main(self):
        url_list, headers2 = self.construct()
        headers1 = self.construct_headers()
        for (url, header1, header2) in zip(url_list, headers1, headers2):
            node_list = self.get_data(url, header1)
            for node in node_list:
                urls = self.get_company_url(node, header2)
                self.save_url(urls)


if __name__ == '__main__':
    crawl = Crawl()
    crawl.main()
