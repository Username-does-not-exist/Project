import requests


class IPool(object):

    def __init__(self):
        self._proxy_api_url = 'http://127.0.0.1:5010/get/'
        self._delete_proxy_base_url = 'http://127.0.0.1:5010/delete/?proxy={}'
        self._all_proxy = 'http://127.0.0.1:5010/get_all/'
        self._count_proxy = 'http://127.0.0.1:5010/get_status/'

    def get_proxy(self):
        proxy = requests.get(self._proxy_api_url).text
        return proxy

    def delete_proxy(self,proxy):
        delete_proxy_url = self._delete_proxy_base_url.format(proxy)
        requests.get(delete_proxy_url)

    def get_all_proxy(self):
        return requests.get(self._all_proxy).text

    def get_proxy_count(self):
        return requests.get(self._count_proxy).text

# if __name__ == '__main__':
#     A = IPool()
#     print(A.get_all_proxy())