import sys
import os
from ctypes import *
sys.path.append(os.path.abspath(os.path.dirname(os.getcwd())))
from cfg.config import *

print('>>>正在初始化...')
YDMApi = windll.LoadLibrary('yundamaAPI')

appId = APP
appKey = KEY
username = USERNAME
password = PASSWORD
codetype = TYPE
timeout = 5
# 验证码文件路径
filename = b'create.jpg'


def verify_code(username, password, appId, appKey, filename, codetype, timeout):
    print('\r\n>>>正在一键识别...')
    result = c_char_p(b"                              ")
    id = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)
    # 分配30个字节存放识别结果
    return id, result.value


id, code = verify_code(username, password, appId, appKey, filename, codetype, timeout)
print("识别结果为{}".format(code.decode('utf-8')))