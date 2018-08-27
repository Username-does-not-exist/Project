import random
import time

from pymongo import MongoClient
import redis
from selenium import webdriver


class FeiPinW(object):

    def __init__(self):
        self.base_url = "http://www.zgfp.com/search/searchcomp.aspx?page={}&ChannelId=20&cid=0&k=&w=&e=1&d=&a="
        self.driver = webdriver.Firefox()
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    def parse_page(self):
        """
        解析数据
        :return:
        """
        company_list = self.driver.find_elements_by_xpath('//*[@id="plList"]/div/table//tr/td[3]/a')
        contact_list = self.driver.find_elements_by_xpath('//*[@id="plList"]/div/table//tr/td[4]')
        number_list = self.driver.find_elements_by_xpath('//*[@id="plList"]/div/table//tr/td[5]')
        address_list = self.driver.find_elements_by_xpath('//*[@id="plList"]/div/table//tr/td[2]')
        type_list = self.driver.find_elements_by_xpath('//*[@id="plList"]/div/table//tr/td[1]')
        item_list = list()
        length = len(company_list)
        for i in range(length):
            try:
                item = dict()
                item['company'] = company_list[i].text
                item['contact'] = contact_list[i].text
                item['number'] = number_list[i].text
                item['address'] = address_list[i].text
                item['type'] = type_list[i].text
                item_list.append(item)
            except Exception as e:
                print(e)
                pass
        return item_list

    def save_data(self, data):
        """
        保存数据
        :param data:
        :return:
        """
        try:
            db = self.conn.FeiPinW
            col = db.FP
            col.insert(data)
            count = col.count()
            print("<|---------------=================----------------|>")
            print("当前已抓取{}条数据".format(count))
        except Exception as e:
            print(e)

    def run(self):
        for i in range(1, 2342):
            url = self.base_url.format(i)
            # t1 = time.time()
            # runtime = random.randint(10, 20)
            self.driver.get(url)
            # t2 = time.time()
            # if t2 - t1 >= runtime:
            #     print("程序暂停运行{}秒-------------------".format(runtime))
            #     time.sleep(runtime)
            #     t1 = 0
            #     t1 = 0
            self.driver.implicitly_wait(6)
            data_list = self.parse_page()
            for data in data_list:
                self.save_data(data)


if __name__ == '__main__':
    FW = FeiPinW()
    FW.run()