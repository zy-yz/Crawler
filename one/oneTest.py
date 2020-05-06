# -*- coding:utf-8 -*-

from urllib import request, parse


# 下载这个网页的源代码
# resp = request.urlopen("http://www.baidu.com")
# print(resp.read())

# 将这个网页下载下来，并且保存为baidu.html
# request.urlretrieve('http://www.baidu.com','baidu.html')

#parse_qs将经过编码后的url进行解码
params = {'name':'张三',"age":18,'greet':'hello world'}
qs = parse.urlencode(params)
result = parse.parse_qs(qs)
print(result)

#urlencode进行加编码
resultEncode = parse.urlencode(params)
print(resultEncode)