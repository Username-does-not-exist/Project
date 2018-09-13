"""
获取企业url对应的xpath://*[@id="list_item"]/div[1]/div/div/div[3]/h2/a

联系方式页面url = company_url + "contactusNews.aspx"


"""
import redis
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver import ActionChains


class Crawl(object):

    def __init__(self):
        self.start_url = "http://www.feijiu.net/gq/s/g1p{}k%b7%cf%d6%bd/"
        self.login_url = "http://www.feijiu.net/login.aspx"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()
        self.Host = "127.0.0.1"
        self.Port = 27017
        self.rPort = 6379
        client = MongoClient(host=self.Host, port=self.Port)
        self.rConn = redis.Redis(host=self.Host, port=self.rPort)
        self.db = client.FJgy
        self.collection = self.db.gy

    def construct_url(self):
        url_list = []
        for i in range(1, 20):
            url = self.start_url.format(i)
            url_list.append(url)
        return url_list

    def get_company_url(self, url):
        """
        获取公司详情页联系方式的url
        :param url:
        :return:
        """

    def login_and_cookies(self):
        """
        处理登陆逻辑
        :return:
        """
        # 登陆
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(5)
        # 输入账号
        username = self.driver.find_element_by_xpath('//*[@id="txt_uname"]')
        ActionChains(self.driver).move_to_element(username)
        username.click()
        username.send_keys("zhuzhu1991")
        self.driver.implicitly_wait(10)
        # 输入密码
        password = self.driver.find_element_by_xpath('//*[@id="txt_pass"]')
        ActionChains(self.driver).move_to_element(password)
        password.send_keys('zhu741852')
        # 点击登陆
        login_button = self.driver.find_element_by_xpath('//*[@id="btn1"]')
        login_button.click()
        self.driver.implicitly_wait(5)
        cookies = self.driver.get_cookies()
        return cookies
    
    def get_contact_info(self, url, cookies):
        """
        获取公司信息
        :param url:
        :param cookies:
        :return:
        """

    def save_data(self, data, contact_info_picture):
        """
        保存数据
        :param data:
        :param contact_info_picture:
        :return:
        """

    def main(self):
        """
        处理抓取逻辑
        :return:
        """
        cookies =  self.login_and_cookies()
        url_list = self.construct_url()
        for url in url_list:
            company_url_list = self.get_company_url(url)
            for company_url in company_url_list:
                company_info, contact_info_picture = self.get_contact_info(company_url, cookies)
                self.save_data(company_info, contact_info_picture)


if __name__ == '__main__':
    crawl = Crawl()
    crawl.main()