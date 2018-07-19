# from multiprocessing import Process, Pool
# import os
# import time
#
#
# def run_proc(wTime):
#     n = 0
#     while n < 3:
#         print("subProcess %s run," % os.getpid(), "{0}".format(time.ctime()))
#         time.sleep(wTime)
#         n += 1
#
#
# if __name__ == "__main__":
#     p = Process(target=run_proc, args=(2,))
#     p.daemon = True
#     p.start()
#     # 加入join方法
#     p.join()
#     print("Parent process run. subProcess is ", p.pid)
#     print("Parent process end,{0}".format(time.ctime()))
from multiprocessing import Process, Pool
import os
import time


def run_proc(name):
    # 定义一个函数用于进程调用
    # 执行一次该函数共需1秒的时间
    for i in range(5):
        # 休眠0.2秒
        time.sleep(0.2)
        print('Run child process %s (%s)' % (name, os.getpid()))


if __name__ == '__main__':
    # 执行主进程
    print('Run the main process (%s).' % (os.getpid()))
    mainStart = time.time()
    # 记录主进程开始的时间
    p = Pool(8)
    # 开辟进程池
    for i in range(16):
        # 开辟14个进程
        p.apply_async(run_proc, args=('Process'+str(i),))
        # 每个进程都调用run_proc函数，
        # args表示给该函数传递的参数。
    print('Waiting for all subprocesses done ...')
    # 关闭进程池
    p.close()
    # 等待开辟的所有进程执行完后，主进程才继续往下执行
    p.join()
    print('All subprocesses done')
    # 记录主进程结束时间
    mainEnd = time.time()
    # 主进程执行时间
    print('All process ran %0.2f seconds.' % (mainEnd-mainStart))