import redis
from pymongo import MongoClient


class CrawlMessage(object):

    def __init__(self):
        rhost = "127.0.0.1"
        rport = "6379"
        self.RedisClint = redis.Redis(host=rhost, port=rport)
        mhost = '127.0.0.1'
        mport = '27017'
        Client = MongoClient(host=mhost, port=mport)
        self.db = Client.gongqiu
        self.collection = self.db.gq

    def get_data(self):
        pass

    def save_data(self):
        pass

    def main(self):
        pass


if __name__ == '__main__':
    crawl = CrawlMessage()
    crawl.main()