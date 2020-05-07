
import requests

data = {
    'first': "true",
    'pn': '1',
    'kd': 'python'
}

headers ={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",

    "Referer": "https://www.lagou.com/jobs/list_Python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
    "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8"
}

response = requests.post('https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=0',
                         data=data,headers=headers)
print(response.text)