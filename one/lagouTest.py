from urllib import request,parse


url = "https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 '
                   '(KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_Java/p-city_0?px=default',
    'Origin' : 'https://www.lagou.com',
    "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8"
 
    }

data = {
    'first': 'true',
    'pn': 1,
    'kd': 'java'
}

req = request.Request(url,headers=headers,
                      data=parse.urlencode(data).encode('utf-8'),method='POST')

resq = request.urlopen(req)
print(resq.read().decode('utf-8'))