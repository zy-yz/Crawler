# encoding= utf-8

import requests
from lxml import etree
from urllib import request
import os
import re

def parse_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)'
                     ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url,headers = headers)
    text = response.text
    # print(text)
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
   # print(imgs)
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r'[\?？\.，。!！~\*]','',alt)
        suffix = os.path.splitext(img_url)[1]
        filename = alt + suffix
        #print(os.path.abspath('.'))
       # print(filename)
        request.urlretrieve(img_url, 'images/'+filename)

def main():
    for x in range(1,10):
        url ='https://www.doutula.com/photo/list/?page=%d'%x
        # print(url)
        parse_page(url)

if __name__ == '__main__':
    main()