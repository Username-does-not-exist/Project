from UserAgentPool import UAPool
from ProxyPool import IPool

ip = IPool().get_proxy()
ua = UAPool().get()

print(ua)
print(ip)