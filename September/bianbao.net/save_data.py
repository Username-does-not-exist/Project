import json
import re
import time
import redis
import requests
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver import ActionChains


class Save(object):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.start_url = "http://www.feijiu.net/FeiZhi/g1/"
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        self.conn = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)

    # def login(self):
    #     base_url = "http://passport.bianbao.net/login?ltype=login&retUrl=http%3A%2F%2Fwww.bianbao.net%2FsdList_page5.html"
    #     self.driver.get(base_url)
    #     self.driver.implicitly_wait(5)
    #     page = self.driver.page_source
    #     parser = re.compile(u'<input id="imgCode" name="imgCode" type="hidden" value="(\w+)" />', re.S)
    #     imgCode = re.findall(parser, page)[0]
    #     formData = {
    #         "memberDetail.wechatOpenid": "",
    #         "phoneNum": "17348515927",
    #         "password": "zhu741852",
    #         "imgCode": imgCode
    #     }
    #     print(formData)
    #     login_url = "http://passport.bianbao.net/loginSave?isMobile=0"
    #     header = {
    #         "Accept": "application/json, text/javascript, */*; q=0.01",
    #         "Accept-Encoding": "gzip, deflate",
    #         "Accept-Language": "zh-CN,zh;q=0.9",
    #         "Content-Length": "81",
    #         "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    #         "Host": "passport.bianbao.net",
    #         "Origin": "http://passport.bianbao.net",
    #         "Proxy-Connection": "keep-alive",
    #         "Referer": "http://passport.bianbao.net/login?ltype=login&retUrl=http%3A%2F%2Fwww.bianbao.net%2FsdList_page5.html",
    #         "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
    #         "X-Requested-With": "XMLHttpRequest"
    #     }
    #     session = requests.Session()
    #     response = session.post(login_url, data=formData, headers=header)
    #     code = response.status_code
    #     if code == 200:
    #         content = response.text
    #         print(content)

    def get_data(self, url):
        """
        联系人：/html/body/div[5]/div[2]/div/div/ul/li[1]/div/p[2]
        电话：/html/body/div[5]/div[2]/div/div/ul/li[2]/div/p[2]
        手机号：/html/body/div[5]/div[2]/div/div/ul/li[3]/div/p[2]
        传真：/html/body/div[5]/div[2]/div/div/ul/li[4]/div/p[2]
        QQ：/html/body/div[5]/div[2]/div/div/ul/li[5]/div/p[2]
        微信：/html/body/div[5]/div[2]/div/div/ul/li[6]/div/p[2]
        地址：/html/body/div[5]/div[2]/div/div/div[1]/div/p[2]
        """
        self.driver.get(url)
        Contact_information_element = self.driver.find_element_by_xpath('/html/body/div[5]/div/ul/li[last()-1]/a')
        Contact_information_element.click()
        self.driver.implicitly_wait(5)
        element = self.driver.find_element_by_xpath('//*[@id="telephoneFind"]')
        element.click()
        # 获取企业联系信息
        item = dict()
        item['contact'] = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/ul/li[1]/div/p[2]').text
        item['number'] = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/ul/li[2]/div/p[2]').text
        item['mobile'] = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/ul/li[3]/div/p[2]').text
        item['fix'] = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/ul/li[4]/div/p[2]').text
        item['QQ'] = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/ul/li[5]/div/p[2]').text
        item['weChat'] = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/ul/li[6]/div/p[2]').text
        item['address'] = self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[1]/div/p[2]').text
        print(item)

    def __del__(self):
        self.driver.close()

    def main(self):
        # 登陆
        base_url = "http://passport.bianbao.net/login?ltype=login&retUrl=http%3A%2F%2Fwww.bianbao.net%2FsdList_page5.html"
        self.driver.get(base_url)
        self.driver.implicitly_wait(5)
        username = self.driver.find_element_by_xpath('//*[@id="accountPhoneNum"]')
        ActionChains(self.driver).move_to_element(username)
        username.click()
        username.send_keys("17348515927")
        password = self.driver.find_element_by_xpath('//*[@id="password"]')
        ActionChains(self.driver).move_to_element(password)
        password.click()
        password.send_keys('zhu741852')
        time.sleep(5)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginsubmit"]')
        login_button.click()
        self.driver.implicitly_wait(5)
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        # 获取需要抓取的url列表
        url_list = self.rConn.hgetall('BiBaoUrl')
        for i in url_list:
            url = i.decode('utf-8')
            data = self.get_data(url)


        # 获取需要抓取的url列表
        # url_list = self.rConn.hgetall("BiBaoUrl")
        # for i in url_list:
        #     url = i.decode("utf-8")
        #     self.driver.get(url)


if __name__ == '__main__':
    save = Save()
    save.main()

