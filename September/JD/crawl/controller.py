import time
from selenium import webdriver
import requests
import sys
import os
from io import BytesIO
from PIL import Image
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from cfg.config import *
from pool.ProxyPool import IPool
from db.Save import save_shop_info
from utils.YunDaMa import translate_verify_code


class Crawl(object):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--proxy-server=http://{}'.format(IPool().get_proxy()))
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()

    def get_licence_url(self, shop_url):
        self.driver.get(shop_url)
        url = self.driver.find_element_by_xpath('/*[@class="shopTolal"]/li[2]/a').get_attribute('href')
        license_url = "http:" + url
        return license_url

    def get_verify_code_url(self, licence_url):
        """
        进入店铺
        :return:
        """
        self.driver.get(licence_url)
        verify_code_url = self.driver.find_element_by_xpath('//*[@class="verify"]/img').get_attribute('src')
        return verify_code_url

    def get_verify_code(self, verify_code_url):
        path = os.path.abspath(os.path.dirname(os.getcwd()))
        folder = path + "\\captcha"
        if not os.path.exists(folder):
            os.mkdir(folder)
            response = requests.get(verify_code_url)
            image = Image.open(BytesIO(response.content))
            code = translate_verify_code(image)
            return code

    def get_shop_info(self, license_url, verify_code):
        """
        获取店铺信息
        :param license_url:
        :param verify_code:
        :return:
        """
        self.driver.get(license_url)
        code_input_element = self.driver.find_element_by_xpath('//*[@class="inp_verify"]')
        code_input_element.clear()
        code_input_element.send_keys(verify_code)
        conmmit_button = self.driver.find_element_by_xpath('//*[@class="btn"]')
        conmmit_button.click()
        # TODO 提取信息并保存
    def run(self):
        """
        处理主要业务逻辑
        :return:
        """
        self.driver.get(START_URL)
        search = self.driver.find_element_by_xpath('//*[@class="form"]/input')
        button = self.driver.find_element_by_xpath('//*[@class="form"]/button')
        search.clear()
        search.send_keys(KEY_WORD)
        button.click()
        time.sleep(2)
        while True:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(5)
            self.driver.refresh()
            shop_elements = self.driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li/div/div[last()-1]/span/a')
            print(len(shop_elements))
            for shop in shop_elements:
                shop_url = shop.get_attribute('href')
                license_url = self.get_licence_url(shop_url)
                verify_code_url = self.get_verify_code_url(license_url)
                verify_code = self.get_verify_code(verify_code_url)
                shopinfo = self.get_shop_info(license_url, verify_code)
                save_shop_info(shop)
            next_page_element = self.driver.find_element_by_xpath('//*[@class="p-num"]/a[last()]')
            if next_page_element.text == "下一页>":
                next_page_element.click()
            else:
                print("抓取完成")
                break


if __name__ == '__main__':
    crawl = Crawl()
    crawl.run()