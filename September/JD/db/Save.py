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

