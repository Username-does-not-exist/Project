import re
import redis
import gevent
from gevent.queue import Queue
from selenium import webdriver
from pymongo import MongoClient


class Waim(object):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    Host = "127.0.0.1"
    Port = 27017
    rPort = 6379
    conn = MongoClient(host=Host, port=Port)
    rConn = redis.Redis(host=Host, port=rPort)

    def __init__(self):
        pass

    @classmethod
    def get_url(self, q):
        urls = self.rConn.hgetall('url_88wm')
        q.put(urls)

    @staticmethod
    def translate(li, result):
        """
        解析数据
        :param li:
        :param result:
        :return:
        """
        a = str(li)
        a_str = a.replace('[', '').replace(']', '').replace("'", '')

        a_list = a_str.split("：")
        b_list = list()
        for i in a_list:
            li = i.split('\\n')
            for i in li:
                j = i.replace('', '')
                b_list.append(j)

        c_list = list()
        for i in b_list:
            if i == '':
                pass
            else:
                c_list.append(i)

        for i in c_list:
            try:
                item1 = re.findall(result, i)[0]
                item2 = c_list.index(item1)
                num = item2 + 1
                company = c_list[num]
                return company
            except Exception as e:
                pass


    @classmethod
    def get_data(self, q):
        """
        获取数据
        :param url:
        :param proxy:
        :return:
        """
        urls = q.get()
        for i in urls:
            try:
                url = i.decode("utf-8")
                self.driver.get(url)
                self.driver.implicitly_wait(10)
                button = self.driver.find_element_by_xpath('//*[@class="meun"]/a[last()]|//*[@class="navigation"]/ul/li[last()]|//*[@class="nav"]/ul/li[last()-1]|//*[@class="vip_nav"]//li[3]')
                button.click()
                self.driver.implicitly_wait(5)
                data_list = self.driver.find_elements_by_xpath('//*[@class="site"]/ul|//*[@class="contact-text"]|//*[@class="address"]/ul|//*[@class="co_Details cf"]')
                massage = list()
                for data in data_list:
                    item = data.text
                    massage.append(item)

                items = dict()
                items['company'] = self.translate(massage, "公司名称")
                items['contact'] = self.translate(massage, '联系人')
                items['mobile'] = self.translate(massage, '移动电话')
                if items['mobile'] == None:
                    items['mobile'] = self.translate(massage, "手机")
                    if items['mobile'] == None:
                        items['mobile'] = self.translate(massage, "手机号")
                items['number'] = self.translate(massage, '公司电话')
                if items['number'] == None:
                    items['number'] = self.translate(massage, '电话')
                items['address'] = self.translate(massage, '公司地址')
                if items['address'] == None:
                    items['address'] = self.translate(massage, '地址')
                items['wechat'] = self.translate(massage, '微信')
                if items['wechat'] == None:
                    items['wechat'] = self.translate(massage, '微信咨询')
                items['qq'] = self.translate(massage, 'QQ')
                if items['qq'] == None:
                    items['qq'] = self.translate(massage, "QQ咨询")
                items['fax'] = self.translate(massage, '传真')
                if items['fax'] == None:
                    items['fax'] = self.translate(massage, '公司传真')
                items['post_number'] = self.translate(massage, "邮编")
                if items['post_number'] == None:
                    items['post_number'] = self.translate(massage, "公司邮编")

                db = self.conn.hy88
                col = db.wm
                col.insert(items)
                print(items)
            except Exception as e:
                print(e)
                pass


if __name__ == '__main__':
    q = Queue()
    pool = list()

    wm = Waim()
    gevent.joinall([
        gevent.spawn(wm.get_url, q),
        gevent.spawn(wm.get_data, q)
    ])

