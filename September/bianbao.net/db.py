from configparser import ConfigParser
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
pwd = os.path.split(os.path.realpath(__file__))[0]
print(pwd)
# class DB(object):
#
#     def __init__(self):
#         _type = None
#