# encoding: utf-8
from urllib import request

# 没有使用代理的

url = 'http://httpbin.org/ip'
resp = request.urlopen(url)
print(resp.read())

#使用代理的
#1.使用proxyhandler,传入一个代理构建一个handler
handler = request.ProxyHandler({"http":"118.181.226.166:44640"})
#2.使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
#3.使用opener构建一个请求
resp1 = opener.open(url)
print(resp1.read())

# ProxyHandler处理器(代理)
# 1.代理的原理:在请求目的网站之前，先请求代理服务器，然后让代理服务器去请求谜底网站，代理服务器拿到目的网站数据后，在转发给我们代码
# 2.http://httpbin.org:这个网站可以查看一些HTTP请求参数
# 3.在代码中使用代理
#     1），使用urllib.request.ProxyHandler,传如一个代理，这个代理是一个字典，key一般是HTTP或者HTTPS。值是"ip:port"
#     2),使用上一步创建的handler,以及"request.build_opener"传建一个"opener"对象
#     3），使用上一步的opener，调用open函数，发送请求
