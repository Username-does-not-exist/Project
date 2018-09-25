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
from db.Save import save_shop_info, save_shop_url, get_shop_url_list
# from utils.YunDaMa import decode_verify_code


class Crawl(object):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--proxy-server=http://{}'.format(IPool().get_proxy()))
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()

    def get_shop_info(self, shop_url):
        """
        获取店铺信息
        :return:
        """
        # 获取店铺详情页
        self.driver.get(shop_url)
        url = self.driver.find_element_by_xpath('/*[@class="shopTolal"]/li[2]/a').get_attribute('href')
        license_url = "http:" + url
        # 营业执照信息所在页面
        self.driver.get(license_url)
        verify_code_url = self.driver.find_element_by_xpath('//*[@class="verify"]/img').get_attribute('src')
        # 创建用于存储验证码图片的文件夹
        path = os.path.abspath(os.path.dirname(os.getcwd()))
        folder = path + "\\captcha"
        if not os.path.exists(folder):
            os.mkdir(folder)
        # 获取验证码图片字节流
        response = requests.get(verify_code_url)
        contant = response.content
        image = Image.open(BytesIO(response.content))
        # 使用第三方打码平台进行验证码识别
        id, verify_code = decode_verify_code(contant)
        # 输入验证码进入营业执照展示页面
        code_input_element = self.driver.find_element_by_xpath('//*[@class="inp_verify"]')
        code_input_element.clear()
        code_input_element.send_keys(verify_code)
        conmmit_button = self.driver.find_element_by_xpath('//*[@class="btn"]')
        conmmit_button.click()
        self.driver.implicitly_wait(2)
        # 提取营业执照信息
        shop_info = dict()
        shop_info['company'] = self.driver.find_element_by_xpath('//*[@class="jScore"]/ul/li[3]/span').text
        shop_info['rgs_number'] = self.driver.find_element_by_xpath('//*[@class="jScore"]/ul/li[4]/span').text
        shop_info['legal_representative'] = self.driver.find_element_by_xpath('//*[@class="jScore"]/ul/li[5]/span').text
        shop_info['rgs_address'] = self.driver.find_element_by_xpath('//*[@class="jScore"]/ul/li[6]/span').text
        shop_info['rgs_capital'] = self.driver.find_element_by_xpath('//*[@class="jScore"]/ul/li[7]/span').text
        shop_info['valid_period'] = self.driver.find_element_by_xpath('//*[@class="jScore"]/ul/li[8]/span').text
        shop_info['business_scope'] = self.driver.find_element_by_xpath('//*[@class="jScore"]/ul/li[9]/span').text
        shop_info['address'] = self.driver.find_element_by_xpath('//*[@class="jScore"]/ul/li[10]/span').text
        shop_info['shop'] = self.driver.find_element_by_xpath('//*[@class="jScore"]/ul/li[11]/span').text
        shop_info['shop_url'] = self.driver.find_element_by_xpath('//*[@class="jScore"]/ul/li[12]/span').text
        # 保存验证码图片
        image.save(folder + '/{}.jpg'.format(shop_info['shop']))
        return shop_info

    def run(self):
        """
        处理主要业务逻辑
        :return:
        """
        for key in KEYS:
            try:
                self.driver.get(START_URL)
                search = self.driver.find_element_by_xpath('//*[@class="form"]/input')
                button = self.driver.find_element_by_xpath('//*[@class="form"]/button')
                search.clear()
                search.send_keys(key)
                button.click()
                time.sleep(2)
                # 获取店铺详情页url
                while True:
                    self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                    time.sleep(5)
                    # self.driver.refresh()
                    shop_elements = self.driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li/div/div[last()-1]/span/a')
                    print("当前页面抓取到{}个店铺".format(len(shop_elements)))
                    for shop in shop_elements:
                        shop_url = shop.get_attribute('href')
                        save_shop_url(shop_url)
                        # shopinfo = self.get_shop_info(shop_url)
                        # save_shop_info(shopinfo)
                    next_page_element = self.driver.find_element_by_xpath('//*[@class="p-num"]/a[last()]')
                    end_element = self.driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[1]/a[last()-1]')
                    next_page_element.click()
                    if end_element.text == 100:
                        print("{}类别的店铺url抓取完成".format(key))
                        break
            except Exception as e:
                print(e)
                pass
        print("所有类别店铺url抓取完成")
        # 抓取店铺营业执照信息
        # url_list = get_shop_url_list()
        # for url in url_list:
        #     shopinfo = self.get_shop_info(url)
        #     save_shop_info(shopinfo)


if __name__ == '__main__':
    crawl = Crawl()
    crawl.run()