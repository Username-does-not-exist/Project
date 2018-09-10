import time

import redis
import requests
from pymongo import MongoClient
from selenium import webdriver


class Save(object):

    # def __init__(self):
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver = webdriver.Chrome()
        # self.start_url = "http://www.feijiu.net/FeiZhi/g1/"
        # self.Host = "127.0.0.1"
        # self.Port = 27017
        # self.rPort = 6379
        # self.conn = MongoClient(host=self.Host, port=self.Port)
        # self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    def login(self):
        login_url = "http://passport.bianbao.net/loginSave?isMobile=0"

        formData = {
            "memberDetail.wechatOpenid":"",
            "iphoneNum": "17348515927",
            "password": "zhu741852",
            "mgCode": "u7UP"
        }

        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Host": "passport.bianbao.net",
            "Proxy-Connection": "keep-alive",
            "Referer": "http://www.bianbao.net/sdList_page5.html",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
        }

        session = requests.session()
        response = session.post(login_url, data=formData, headers=header)
        code = response.status_code
        if code == 200:
            print(response.cookies)

    def get_data(self):
        pass

    # def __del__(self):
        # self.driver.close()

    def main(self):
        # 登陆
        self.login()
        # base_url = "http://www.bianbao.net/sdList_page1.html"
        # self.driver.get(base_url)
        # self.driver.implicitly_wait(5)
        # login_element = self.driver.find_element_by_xpath('//*[@id="li_1"]/a')
        # login_element.click()
        # self.driver.implicitly_wait(5)
        # username = self.driver.find_element_by_xpath('//*[@class="reg_li1 positionR"][1]/input')
        # username.clear()
        # username.send_keys("17348515927")
        # password = self.driver.find_element_by_xpath('//*[@class="reg_li1 positionR"][2]/input')
        # password.clear()
        # password.send_keys('zhu741852')
        # login_button = self.driver.find_element_by_xpath('//*[@id="loginsubmit"]')
        # login_button.click()
        # self.driver.implicitly_wait(5)

        # 获取需要抓取的url列表
        # url_list = self.rConn.hgetall("BiBaoUrl")
        # for i in url_list:
        #     url = i.decode("utf-8")
        #     self.driver.get(url)


if __name__ == '__main__':
    save = Save()
    save.main()

