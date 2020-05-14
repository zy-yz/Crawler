#encoding: utf-8

import requests
from lxml import etree
import time
import re

HEADERS = {

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",

        "Referer": "https://www.lagou.com/jobs/list_Python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput=",
        "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8"
}

def request_list_page():

    url = 'https://www.lagou.com/jobs/list_python?city=%E5%85%A8%E5%9B%BD&cl=false&fromSearch=true&labelWords=&suginput='
    data = {
        'first' : "false",
        'pn': 1,
        'kd':'python'
    }

    for x in range(1,14):
        data['pn'] = x
        response = requests.post(url,headers = HEADERS,data = data)
        # json方法:如果返回来的是json数据，那么这个方法会自动的load成字典
        result = response.json()
        positions = result['content']['positionResult']['result']
        for position in positions:
            positionId = position['positionId']
            position_url = 'https://www.lagou.com/jobs/%s.html' %positionId
            parse_position_detail(position_url)
            break
        break

def parse_position_detail(url):
    response = requests.get(url,headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    # 这需要验证
    position_name = html.xpath("//div[@class='job-name']//h1")[0]
    # position_name = html.xpath("//span[@class='name]/text")[0]
    job_request_spans = html.xpath("//dd[@class='job_request']//span")
    salary = job_request_spans[0].xpath('.//text()')[0].strip()
    city = job_request_spans[1].xpath(".//text()")[0].strip()
    city = re.sub(r"\s/","",city)
    work_years = job_request_spans[2].xpath(".//text()")[0].strip()
    work_years = re.sub(r"[\s/]]","",work_years)
    eduction = job_request_spans[3].xpath(".//text()")[0].strip()
    eduction = re.sub(r"[\s/]]", "", eduction)
    desc = "".join(html.xpath("//dd[@class='job_bt']//text()")).strip()
    print(desc)

def main():
    request_list_page()

if __name__ == '__main__':
    main()