import requests

#   使用代理，只要在请求方法中传递参数proxies就可以了
proxy = {
    'http':'121.196.205.196:8888'
}
response = requests.get("http://httpbin.org/ip",proxies=proxy)
print(response.text)