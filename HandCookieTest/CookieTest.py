# encoding: utf-8

# cookie中参数的意义
#     Name:cookie的名字
#     VALUE：cookie的值
#     EXpirse:cookie的过期时间
#     Path:Cookie的作用路径
#     Domain:cookie作用的域名
#     SECURE:是否只在HTTPS协议下起作用

from urllib import request
from urllib import parse
from http.cookiejar import CookieJar

# 1.登录
# 1.1创建一个CookieJar对象
cookiejar = CookieJar()
#1.3使用cookiejar创建一个HTTPCookieProcess对象
handler = request.HTTPCookieProcessor(cookiejar)
#1.3使用上一步创建的handler创建一个opener
opener = request.build_opener(handler)
#1.4使用opener发送登录的请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; '
                  'Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
data = {
    'email': '18716872350',
    'password': 'renren123456'
}
login_url = "http://www.renren.com/PLogin.do"
req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
request.urlopen(req)

# 2.访问个人主页
dapeng_url = "http://www.renren.com/880151247/profile"
# 获取个人主页的页面的时候，不要新建opener
# 应该使用之前的opener，因为之前的包含了cookie信息
req = request.Request(dapeng_url, headers=headers)
resp = opener.open(req)
with open('renren.html', 'w', encoding='utf-8') as fp:
    fp.write(resp.read().decode('utf-8'))