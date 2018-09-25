import sys
import os
from ctypes import *
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from cfg.config import *

print('>>>正在初始化...')
YDMApi = windll.LoadLibrary('yundamaAPI')

appId = APPID
appKey = APPKEY
username = USERNAME
password = PASSWORD
codetype = TYPE
timeout = 5
# 验证码文件路径
filename = b'create.jpg'


def decode_verify_code(username, password, appId, appKey, filename, codetype, timeout):
    print('\r\n>>>正在一键识别...')
    # 分配30个字节存放识别结果
    result = c_char_p(b"                              ")
    id = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
    # id = YDMApi.YDM_EasyDecodeByBytes(appId, appKey)
    code = result.value.decode('utf-8')
    return id, code


id, code = decode_verify_code(username, password, appId, appKey, filename, codetype, timeout)
# print("识别结果为{}".format(code))
print(id, code)