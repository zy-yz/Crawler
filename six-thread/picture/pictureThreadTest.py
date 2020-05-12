# encoding= utf-8
import threading
from queue import Queue

import requests
from lxml import etree
from urllib import request
import os
import re

class Producer(threading.Thread):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)'
                     ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Producer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queuq = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self,url):
        response = requests.get(url, headers=self.headers)
        text = response.text
        # print(text)
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
        # print(imgs)
        for img in imgs:
            img_url = img.get('data-original')
            alt = img.get('alt')
            alt = re.sub(r'[\?？\.，。!！~\*]', '', alt)
            suffix = os.path.splitext(img_url)[1]
            filename = alt + suffix
            # print(os.path.abspath('.'))
            # print(filename)
            self.img_queuq.put((img_url,filename))

class Consumer(threading.Thread):
    def __init__(self,page_queue,img_queue,*args,**kwargs):
        super(Consumer,self).__init__(*args,**kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty() and self.page_queue.empty():
                break
            img_url,filename = self.img_queue.get()
            request.urlretrieve(img_url,'images/'+filename)
            print(filename+'下载完成！')



def main():
    page_queue = Queue(100)
    img_queue = Queue(1000)
    for x in range(1, 10):
        url = 'https://www.doutula.com/photo/list/?page=%d' % x
        page_queue.put(url)

    for x in range(5):
         t = Producer(page_queue,img_queue)
         t.start()

    for x in range(5):
        t = Consumer(page_queue,img_queue)
        t.start()

if __name__ == '__main__':
    main()



