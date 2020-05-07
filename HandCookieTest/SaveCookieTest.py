# encoding: utf-8

from urllib import request
from http.cookiejar import  MozillaCookieJar

#   将cookie信息保存到文件中
cookiejar = MozillaCookieJar('cookie.txt')

#这一行是将cookie读取出来
cookiejar.load(ignore_discard=True)
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

# resp = opener.open('http://www.baidu.com/')
# cookiejar.save()

resp1 = opener.open('http://httpbin.org/cookies')
# 对于会话退出就没有cookie信息的就可以设置这个参数，同时也可以保存信息了
#   cookiejar.save(ignore_discard=True)

for cookie in cookiejar:
    print(cookie)