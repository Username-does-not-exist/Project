import datetime
import hashlib
from datetime import *


def http_upload_image(url, paramKeys, paramDict, filebytes):
    timestr = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    boundary = '------------' + hashlib.md5(timestr.encode("utf-8")).hexdigest().lower()
    boundarystr = '\r\n--%s\r\n' % (boundary)

    bs = b''
    for key in paramKeys:
        bs = bs + boundarystr.encode('ascii')
        param = "Content-Disposition: form-data; name=\"%s\"\r\n\r\n%s" % (key, paramDict[key])

        # print param
        bs = bs + param.encode('utf8')
    bs = bs + boundarystr.encode('ascii')

    header = 'Content-Disposition: form-data; name=\"image\"; filename=\"%s\"\r\nContent-Type: image/gif\r\n\r\n' % (
        'sample')
    bs = bs + header.encode('utf8')

    bs = bs + filebytes
    tailer = '\r\n--%s--\r\n' % (boundary)
    bs = bs + tailer.encode('ascii')

    import requests
    headers = {'Content-Type': 'multipart/form-data; boundary=%s' % boundary,
               'Connection': 'Keep-Alive',
               'Expect': '100-continue',
               }
    response = requests.post(url, params='', data=bs, headers=headers)
    content = response.text
    code = content.replace('{', '').replace('}', '').split(',')[0].split(':')[1].replace('"', '')
    return code