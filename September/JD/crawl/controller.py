import time
from selenium import webdriver
import sys
import os
from PIL import Image
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from cfg.config import *
from pool.ProxyPool import IPool
from db.Save import save_shop_info, save_shop_url, get_shop_url_list
from db.Del import delURL
from utils.yunsuDaMa import http_upload_image
from cfg.config import *


post_content = {
        'username': username,
        'password': password,
        'typeid': typeid,
        'timeout': timeout,
        'softid': softid,
        'softkey': softkey,
    }

PostUrl = POSTURL
paramKeys = []
for i in post_content.keys():
    paramKeys.append(i)


class CrawlINFO(object):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--proxy-server=http://{}'.format(IPool().get_proxy()))
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome()

    def get_license_url(self, shop_url):
        """
        获取店铺信息
        :return:
        """
        # 获取店铺详情页
        self.driver.get(shop_url)
        self.driver.implicitly_wait(2)
        license_url = self.driver.find_element_by_xpath('//*[@class="shopTolal"]/li[2]/a|//*[@class="licenceIcon"]/a').get_attribute('href')
        shop = self.driver.find_element_by_xpath('//*[@class="jLogo"]/a').text
        return license_url, shop

    def get_verify_code(self, license_url, shop):
        """
        获取验证码截图并保存
        :param license_url:
        :return:
        """
        # 营业执照信息所在页面
        self.driver.get(license_url)
        self.driver.implicitly_wait(5)
        time.sleep(1)
        # 创建目录
        path = os.path.abspath(os.path.dirname(os.getcwd()))
        folder = path + "\\captcha"
        if not os.path.exists(folder):
            os.mkdir(folder)
        # 获取验证码截图
        self.driver.save_screenshot(folder + '/{}.png'.format(shop))
        element = self.driver.find_element_by_xpath('//*[@class="verify"]/img')
        # 获取验证码坐标
        left = element.location['x']
        top = element.location['y']
        right = element.location['x'] + element.size['width']
        bottom = element.location['y'] + element.size['height']
        # 保存截图
        im = Image.open(folder + '/{}.png'.format(shop))
        im = im.crop((left, top, right, bottom))
        im.save(folder + '/{}.png'.format(shop))

    def parse_verify_code(self, shop):
        """
        获取验证码并保存
        :param shop:
        :return:
        """
        # # 创建用于存储验证码图片的文件夹
        # path = os.path.abspath(os.path.dirname(os.getcwd()))
        # folder = path + "\\captcha"
        # if not os.path.exists(folder):
        #     os.mkdir(folder)
        # # 获取验证码图片字节流
        # response = requests.get(verify_code_url)
        # # 保存验证码图片
        # image = Image.open(BytesIO(response.content))
        # image.save(folder + '/{}.jpg'.format(shop))
        # # 返回验证码的二进制数据

        file = os.path.dirname(os.getcwd()) + '\\captcha\{}.png'.format(shop)
        fileBytes = open(file, 'rb').read()
        return fileBytes

    def parse_data(self, verify_code):
        # 输入验证码进入营业执照展示页面
        code_input_element = self.driver.find_element_by_xpath('//*[@class="inp_verify"]')
        code_input_element.clear()
        code_input_element.send_keys(verify_code)
        conmmit_button = self.driver.find_element_by_xpath('//*[@class="btn"]')
        conmmit_button.click()
        self.driver.implicitly_wait(5)
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
        print(shop_info)
        return shop_info

    def __del__(self):
        self.driver.close()


if __name__ == '__main__':
    info = CrawlINFO()
    # 抓取店铺营业执照信息
    url_list = get_shop_url_list()
    for url in url_list:
        shop_url = url.decode('utf-8')
        try:
            license_url, shop = info.get_license_url(shop_url)
            info.get_verify_code(license_url,shop)
            verify_code_bytes = info.parse_verify_code(shop)
            verify_code = http_upload_image(PostUrl, paramKeys, post_content, verify_code_bytes)
            shop_info = info.parse_data(verify_code)
            save_shop_info(shop_info)
            delURL('jd_sm_shop_urls', url)
        except Exception as e:
            print(e)
            print(shop_url)
            pass