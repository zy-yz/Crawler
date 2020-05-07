
import requests

#   发送post请求，
#   直接调用requests.post就可以了
#   如果返回的是json数据，那么可以调用response.json()将json字符串转换为字典或者列表

# params接受一个字典或者字符串中的查询参数，字典类自动转换为URL编码，不需要urlencode()
response = requests.get("http://www.baidu.com/")
print(type(response.text))
#查看响应内容，返回的是Unicode的数据
print(response.text)
print(type(response.content))
# 查看响应内容，返回的是字节流数据
print(response.content.decode('utf-8'))

#   text和content的区别
#   1.text是直接从网络上抓取的数据，没有进过解码
#   2.content是str的数据类型，将content进行解码的字符串，解码需要指定一个编码方法，否则猜测，有可能会产生编码错误的问题

print(response.url)
print(response.encoding)
print(response.status_code)

params = {
    'wd': '中国'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; '
                  'Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}


response = requests.get("http://www.baidu.com/s",params=params,headers=headers)

with open('baidu.html','w',encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))
print(response.url)