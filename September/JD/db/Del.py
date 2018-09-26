import redis
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from cfg.config import *


def delURL(key, value):
    if value is not None:
        conn = redis.Redis(host=HOST, port=RPORT)
        conn.hdel(key, value)


