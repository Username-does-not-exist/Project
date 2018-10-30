from pymongo import MongoClient
import redis
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from cfg.config import *


def save_shop_info(item):
    if item is not None:
        client = MongoClient(host=HOST, port=MPORT)
        db = client.JD
        col = db.shop
        col.insert(item)


def save_shop_url(url):
    if url is not None:
        conn = redis.Redis(host=HOST, port=RPORT)
        conn.hset(redis_col_name, url, 0)


def get_shop_url_list():
    conn = redis.Redis(host=HOST, port=RPORT)
    url_list = conn.hgetall('jd-shop-urls')
    return url_list