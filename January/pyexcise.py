import logging


# 1.生成器
def start():
    for i in range(5):
        yield i


a = start()
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


def fib(n):
    step = 0
    num1, num2 = 0, 1
    while step < n:
        print(num1)
        num1, num2 = num2, num1+num2
        step += 1


fib(10)

# 2.迭代器

li = [x for x in range(10)]
print(li)

add = lambda x, y: print(x/y)
add(1, 2)

# 3.装饰器


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            else:
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator


@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)


foo()


a = tuple()


class SingleMode():

    def __init__(self):
        pass

    def __getattr__(self, item):
        pass

    def __setattr__(self, key, value):
        pass

    def first(self):
        pass

    def second(self):
        pass

    def third(self):
        pass

    def __del__(self):
        print("程序运行结束！！！")


if __name__ == '__main__':
    single = SingleMode()



