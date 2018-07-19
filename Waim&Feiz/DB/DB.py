import redis
from pymongo import MongoClient


class DB(object):

    def __init__(self):
        pass

    def mdb(self):
        Host = "127.0.0.1"
        Port = 27017
        conn = MongoClient(host=Host, port=Port)
        return conn

    def rdb(self):
        Host = "127.0.0.1"
        rPort = 6379
        rConn = redis.Redis(host=Host, port=rPort)
        return rConn


if __name__ == '__main__':
    db = DB()