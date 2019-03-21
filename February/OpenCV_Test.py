# # import time
# # from multiprocessing import Process
# #
# # # import cv2
# # # import numpy as np
# # # from matplotlib import pyplot as plt
# # #
# # #
# # # img = cv2.imread("./image/image_01.jpg", 0)
# # #
# # # blur = cv2.blur(img, (5, 5))
# # #
# # # plt.subplot(121), plt.imshow(img), plt.title('Original')
# # # plt.xticks([]), plt.yticks([])
# # # plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
# # # plt.xticks([]), plt.yticks([])
# # # plt.show()
# #
# # class Restaurant(object):
# #
# #     def chef(self, orders):
# #         print("顾客下单了{}个菜".format(orders))
# #         i = 0
# #         while True:
# #             time.sleep(60)
# #             i += 5
# #             print("已经做好了{}个菜".format(i))
# #             if i == orders:
# #                 print("全部菜已做好")
# #                 break
# #
# #     def waiter(self, dishs):
# #         for dish in dishs:
# #             time.sleep(30)
# #             print("送菜完毕！")
# #
# #     def customer(self, nums):
# #         return nums * 2
# #
# #
# # if __name__ == '__main__':
# #     res = Restaurant()
# #
# #     p1 = Process(target=res.customer, args=(200,))
# #     p2 = Process(target=res.waiter, args=(3,))
# #     p3 = Process(target=res.chef, args=(4,))
# #
# #     # orders = res.customer(200)
# #     # dishs = res.chef(orders)
# #     # delivery = res.waiter(dishs)
#
# # from multiprocessing import Manager, Pool, Process, Queue
# # import os, time, random
# #
# #
# # def reader(q):
# #     print("reader启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
# #     for i in range(q.qsize()):
# #         print("reader从Queue获取到消息：%s"%q.get(True))
# #
# #
# # def writer(q):
# #     print("writer启动(%s),父进程为(%s)"%(os.getpid(),os.getppid()))
# #     for i in "dongGe":
# #         q.put(i)
# #
# #
# # # 写数据进程执行的代码:
# # def write(q):
# #     for value in ['A', 'B', 'C']:
# #         print('Put %s to queue...' % value)
# #         q.put(value)
# #         time.sleep(random.random())
# #
# #
# # # 读数据进程执行的代码:
# # def read(q):
# #     while True:
# #         if not q.empty():
# #             value = q.get(True)
# #             print('Get %s from queue.' % value)
# #             time.sleep(random.random())
# #         else:
# #             break
#
#
# # if __name__=='__main__':
# #     # 父进程创建Queue，并传给各个子进程：
# #     print("(%s) start" % os.getpid())
# #     q = Manager().Queue()  # 使用Manager中的Queue来初始化
# #     po = Pool()
# #     # 使用阻塞模式创建进程，这样就不需要在reader中使用死循环了，可以让writer完全执行完成后，再用reader去读取
# #     po.apply(writer, (q,))
# #     po.apply(reader, (q,))
# #     po.close()
# #     po.join()
# #     print("(%s) End" % os.getpid())
# #     print("-----------------------")
# #     q = Queue()
# #     pw = Process(target=write, args=(q,))
# #     pr = Process(target=read, args=(q,))
# #     # 启动子进程pw，写入:
# #     pw.start()
# #     # 等待pw结束:
# #     pw.join()
# #     # 启动子进程pr，读取:
# #     pr.start()
# #     pr.join()
# #     # pr进程里是死循环，无法等待其结束，只能强行终止:
# #     print('')
# #     print('所有数据都写入并且读完')
#
#
# # import pika
# # import time
# # 1
# # # 建立一个实例
# # connection = pika.BlockingConnection(
# #     pika.ConnectionParameters('localhost', 5672)  # 默认端口5672，可不写
# #     )
# # # 声明一个管道，在管道里发消息
# # channel = connection.channel()
# # # 在管道里声明queue
# # channel.queue_declare(queue='hello')
# # # RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
# # channel.basic_publish(exchange='',
# #                       routing_key='hello',  # queue名字
# #                       body='Hello World!')  # 消息内容
# # print(" [x] Sent 'Hello World!'")
# # connection.close()
# #
# #
# # # 建立实例
# # connection = pika.BlockingConnection(pika.ConnectionParameters(
# #                'localhost'))
# # # 声明管道
# # channel = connection.channel()
# #
# # # 为什么又声明了一个‘hello’队列？
# # # 如果确定已经声明了，可以不声明。但是你不知道那个机器先运行，所以要声明两次。
# # channel.queue_declare(queue='hello')
# #
# #
# # def callback(ch, method, properties, body):  # 四个参数为标准格式
# #     print(ch, method, properties)  # 打印看一下是什么
# #     # 管道内存对象  内容相关信息  后面讲
# #     print(" [x] Received %r" % body)
# #     time.sleep(15)
# #     ch.basic_ack(delivery_tag=method.delivery_tag)  # 告诉生成者，消息处理完成
# #
# #
# # channel.basic_consume(  # 消费消息
# #         callback,  # 如果收到消息，就调用callback函数来处理消息
# #         queue='hello',  # 你要从那个队列里收消息
# #         # no_ack=True  # 写的话，如果接收消息，机器宕机消息就丢了
# #         # 一般不写。宕机则生产者检测到发给其他消费者
# #         )
# #
# # print(' [*] Waiting for messages. To exit press CTRL+C')
# # channel.start_consuming()
#
# # import pika
# # import time
# # import threading
# # import os
# # import json
# # import datetime
# # from multiprocessing import Process
# #
# # # rabbitmq 配置信息
# # MQ_CONFIG = {
# #     "host": "localhost",
# #     "port": 5672,
# #     "vhost": "/",
# #     "user": "beyond",
# #     "passwd": "beyond",
# #     "exchange": "ex_change",
# #     "serverid": "eslservice",
# #     "serverid2": "airservice"
# # }
# #
# #
# # class RabbitMQServer(object):
# #     _instance_lock = threading.Lock()
# #
# #     def __init__(self, recv_serverid, send_serverid):
# #         # self.serverid = MQ_CONFIG.get("serverid")
# #         self.exchange = MQ_CONFIG.get("exchange")
# #         self.channel = None
# #         self.connection = None
# #         self.recv_serverid = recv_serverid
# #         self.send_serverid = send_serverid
# #
# #     def reconnect(self):
# #         if self.connection and not self.connection.is_closed():
# #             self.connection.close()
# #
# #         credentials = pika.PlainCredentials(MQ_CONFIG.get("user"), MQ_CONFIG.get("passwd"))
# #         parameters = pika.ConnectionParameters(MQ_CONFIG.get("host"), MQ_CONFIG.get("port"), MQ_CONFIG.get("vhost"),
# #                                                credentials)
# #         self.connection = pika.BlockingConnection(parameters)
# #
# #         self.channel = self.connection.channel()
# #         self.channel.exchange_declare(exchange=self.exchange, exchange_type="direct")
# #
# #         result = self.channel.queue_declare(queue="queue_{0}".format(self.recv_serverid), exclusive=True)
# #         queue_name = result.method.queue
# #         self.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.recv_serverid)
# #         self.channel.basic_consume(self.consumer_callback, queue=queue_name, no_ack=False)
# #
# #     def consumer_callback(self, channel, method, properties, body):
# #         """
# #         消费消息
# #         :param channel:
# #         :param method:
# #         :param properties:
# #         :param body:
# #         :return:
# #         """
# #         channel.basic_ack(delivery_tag=method.delivery_tag)
# #         process_id = os.getpid()
# #         print("current process id is {0} body is {1}".format(process_id, body))
# #
# #     def publish_message(self, to_serverid, message):
# #         """
# #         发布消息
# #         :param to_serverid:
# #         :param message:
# #         :return:
# #         """
# #         message = dict_to_json(message)
# #         self.channel.basic_publish(exchange=self.exchange, routing_key=to_serverid, body=message)
# #
# #     def run(self):
# #         while True:
# #             self.channel.start_consuming()
# #
# #     @classmethod
# #     def get_instance(cls, *args, **kwargs):
# #         """
# #         单例模式
# #         :return:
# #         """
# #         if not hasattr(cls, "_instance"):
# #             with cls._instance_lock:
# #                 if not hasattr(cls, "_instance"):
# #                     cls._instance = cls(*args, **kwargs)
# #         return cls._instance
# #
# #
# # def process1(recv_serverid, send_serverid):
# #     """
# #     用于测试同时订阅和发布消息
# #     :return:
# #     """
# #     # 线程1 用于去 从rabbitmq消费消息
# #     rabbitmq_server = RabbitMQServer.get_instance(recv_serverid, send_serverid)
# #     rabbitmq_server.reconnect()
# #     recv_threading = threading.Thread(target=rabbitmq_server.run)
# #     recv_threading.start()
# #     i = 1
# #     while True:
# #         # 主线程去发布消息
# #         message = {"value": i}
# #         rabbitmq_server.publish_message(rabbitmq_server.send_serverid,message)
# #         i += 1
# #         time.sleep(0.01)
# #
# #
# # class CJsonEncoder(json.JSONEncoder):
# #     def default(self, obj):
# #         if isinstance(obj, datetime.datetime):
# #             return obj.strftime('%Y-%m-%d %H:%M:%S')
# #         elif isinstance(obj, datetime.date):
# #             return obj.strftime("%Y-%m-%d")
# #         else:
# #             return json.JSONEncoder.default(self, obj)
# #
# #
# # def dict_to_json(po):
# #     jsonstr = json.dumps(po, ensure_ascii=False, cls=CJsonEncoder)
# #     return jsonstr
# #
# #
# # def json_to_dict(jsonstr):
# #     if isinstance(jsonstr, bytes):
# #         jsonstr = jsonstr.decode("utf-8")
# #     d = json.loads(jsonstr)
# #     return d
# #
# #
# # if __name__ == '__main__':
# #     recv_serverid = MQ_CONFIG.get("serverid")
# #     send_serverid = MQ_CONFIG.get("serverid2")
# #     # 进程1 用于模拟模拟程序1
# #     p = Process(target=process1, args=(recv_serverid, send_serverid, ))
# #     p.start()
# #
# #     # 主进程用于模拟程序2
# #     process1(send_serverid, recv_serverid)
#
import pika
import threading
import json
import datetime
import os
from gevent import monkey; monkey.patch_socket()
import gevent


from pika.exceptions import ChannelClosed
from pika.exceptions import ConnectionClosed


# rabbitmq 配置信息
MQ_CONFIG = {
    "host": "localhost",
    "port": 5672,
    "vhost": "/",
    "user": "beyond",
    "passwd": "beyond",
    "exchange": "ex_change",
    "serverid": "eslservice",
    "serverid2": "airservice"
}


class RabbitMQServer(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self.recv_serverid = ""
        self.send_serverid = ""
        self.exchange = MQ_CONFIG.get("exchange")
        self.connection = None
        self.channel = None

    def reconnect(self):
        if self.connection and not self.connection.is_closed:
            self.connection.close()

        credentials = pika.PlainCredentials(MQ_CONFIG.get("user"), MQ_CONFIG.get("passwd"))
        parameters = pika.ConnectionParameters(MQ_CONFIG.get("host"), MQ_CONFIG.get("port"), MQ_CONFIG.get("vhost"),
                                               credentials)
        self.connection = pika.BlockingConnection(parameters)

        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange, exchange_type="direct")

        if isinstance(self, RabbitComsumer):
            result = self.channel.queue_declare(queue="queue_{0}".format(self.recv_serverid), exclusive=True)
            queue_name = result.method.queue
            self.channel.queue_bind(exchange=self.exchange, queue=queue_name, routing_key=self.recv_serverid)
            self.channel.basic_consume(self.consumer_callback, queue=queue_name, no_ack=False)


class RabbitComsumer(RabbitMQServer):

    def __init__(self):
        super(RabbitComsumer, self).__init__()

    def consumer_callback(self, ch, method, properties, body):
        """
        :param ch:
        :param method:
        :param properties:
        :param body:
        :return:
        """
        ch.basic_ack(delivery_tag=method.delivery_tag)
        process_id = threading.current_thread()
        print("current process id is {0} body is {1}".format(process_id, body))

    def start_consumer(self):
        while True:
            self.reconnect()
            self.channel.start_consuming()

    @classmethod
    def run(cls, recv_serverid):
        consumer = cls()
        consumer.recv_serverid = recv_serverid
        consumer.start_consumer()


class RabbitPublisher(RabbitMQServer):

    def __init__(self):
        super(RabbitPublisher, self).__init__()

    def start_publish(self):
        self.reconnect()
        i = 1
        while True:
            message = {"value": i}
            message = dict_to_json(message)
            self.channel.basic_publish(exchange=self.exchange, routing_key=self.send_serverid, body=message)
            i += 1

    @classmethod
    def run(cls, send_serverid):
        publish = cls()
        publish.send_serverid = send_serverid
        publish.start_publish()


class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)


def dict_to_json(po):
    jsonstr = json.dumps(po, ensure_ascii=False, cls=CJsonEncoder)
    return jsonstr


def json_to_dict(jsonstr):
    if isinstance(jsonstr, bytes):
        jsonstr = jsonstr.decode("utf-8")
    d = json.loads(jsonstr)
    return d


if __name__ == '__main__':
    recv_serverid = MQ_CONFIG.get("serverid")
    send_serverid = MQ_CONFIG.get("serverid2")
    # 这里分别用两个线程去连接和发送
    threading.Thread(target=RabbitComsumer.run, args=(recv_serverid,)).start()
    threading.Thread(target=RabbitPublisher.run, args=(send_serverid,)).start()
    # 这里也是用两个连接去连接和发送，
    threading.Thread(target=RabbitComsumer.run, args=(send_serverid,)).start()
    RabbitPublisher.run(recv_serverid)


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)

g1.join()
g2.join()
g3.join()