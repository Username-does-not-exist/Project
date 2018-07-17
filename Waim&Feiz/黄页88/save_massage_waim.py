import re
import redis
from selenium import webdriver
from pymongo import MongoClient
import sys
from Pool.ProxyPool import IPool
sys.path.append('./')
from Pool.UserAgentPool import UAPool


class Waim(object):

    def __init__(self):
        # self.driver = webdriver.Firefox()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "User-Agent": UAPool().get()
        }

    def get_porxy(self):
        pro = IPool().get_proxy()
        proxy = {"http": "http://" + pro}
        return proxy, pro

    def translate(self, li, result):
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
            except:
                pass

    def get_data(self):
        """
        获取数据
        :param url:
        :param proxy:
        :return:
        """
        button = self.driver.find_element_by_xpath('//*[@class="meun"]/a[last()]|//*[@class="navigation"]/ul/li[last()]|//*[@class="nav"]/ul/li[last()-1]')
        button.click()
        self.driver.implicitly_wait(5)
        data_list = self.driver.find_elements_by_xpath('//*[@class="site"]/ul|//*[@class="contact-text"]|//*[@class="address"]/ul')
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
            items['fax'] = self.translate(massage, '传真号码')
        items['post_number'] = self.translate(massage, "邮编")
        if items['post_number'] == None:
            items['post_number'] = self.translate(massage, "邮编号码")

        return items

    def save_data(self, data):
        """
        保存数据
        :param data:
        :return:
        """
        try:
            db = self.conn.hy88_wm
            col = db.fz
            if data['contact'] == None:
                pass
            else:
                col.insert(data)
                count = col.count()
                print(data)
                print("<|---------------=================----------------|>")
                print("当前已抓取{}条数据".format(count))
        except Exception as e:
            print(e)

    def main(self):
        urls = self.rConn.hgetall('company_url_88wm')
        for i in urls:
            try:
                url = i.decode('utf-8')
                self.driver.get(url)
                self.driver.implicitly_wait(10)
                data = self.get_data()
                self.save_data(data)
            except Exception as e:
                print(e)
                pass


if __name__ == '__main__':
    w = Waim()
    w.main()



