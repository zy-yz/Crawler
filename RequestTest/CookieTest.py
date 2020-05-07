import  requests

# 如果一个响应中包含了cooike，那么可以利用cookie属性拿到这个返回的cookie值

url = "http://www.renren.com/PLogin.do"
data = {"email":"1090712762@qq.com",'password':"renren123456"}
resp = requests.get("http://www.baidu.com/")
print(resp.cookies)
print(resp.cookies.get_dict())

#   session
# 多个请求共享cookie，这里的session只是一个对话的对象
headers ={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",

    "Referer": "https://www.lagou.com/jobs/list_Python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
    "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8"
}

session = requests.Session()

session.post(url,data=data,headers=headers)
response = session.get('http://www.renren.com/880151247/profile')
with open('renren1.html','w', encoding='utf-8') as fp:
    fp.write(response.text)