from pymongo import MongoClient
import redis
from selenium import webdriver


class FeiPinW(object):

    def __init__(self):
        self.base_url = "http://www.feipinzhan.com/company/index.php?catid=0&areaid=0&groupid=&page={}"
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Firefox()
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
        company_list = self.driver.find_elements_by_xpath('//*[@class="cb insetpaix"]/div[2]/h2/a')
        number_list = self.driver.find_elements_by_xpath('//*[@class="cb insetpaix"]/div[3]/div[3]/span[1]')
        address_list = self.driver.find_elements_by_xpath('//*[@class="cb insetpaix"]/div[2]/dl/dt[2]')
        type_list = self.driver.find_elements_by_xpath('//*[@class="cb insetpaix"]/div[2]/dl/dt[3]')
        item_list = list()
        length = len(company_list)
        for i in range(length):
            try:
                item = dict()
                item['company'] = company_list[i].text
                item['number'] = number_list[i].text
                item['address'] = address_list[i].text.replace('公司地址:', '')
                item['type'] = type_list[i].text.replace('经营范围:', '')
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
            db = self.conn.FeiPinZ
            col = db.FP
            col.insert(data)
            print(data)
        except Exception as e:
            print(e)

    def run(self):
        for i in range(1, 78):
            url = self.base_url.format(i)
            self.driver.get(url)
            self.driver.implicitly_wait(6)
            data_list = self.parse_page()
            for data in data_list:
                self.save_data(data)


if __name__ == '__main__':
    FW = FeiPinW()
    FW.run()