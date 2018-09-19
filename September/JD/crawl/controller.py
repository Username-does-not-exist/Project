import redis
from pymongo import MongoClient
from selenium import webdriver
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from cfg.config import *


class Crawl(object):

    def __init__(self):
        self.login_url = LOGIN_URL
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver = webdriver.Chrome()
        self.client = MongoClient(host=Host, port=MPORT)
        self.rConn = redis.Redis(host=Host, port=RPORT)

