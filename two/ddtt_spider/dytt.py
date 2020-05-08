

from lxml import etree
import requests

BASE_DOMAIN = 'https://www.ygdy8.net'

HEADERS ={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/"
                  "537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36",
    'Referer': "https://www.ygdy8.net/html/gndy/dyzz/list_23_2.html"
}

def get_detail_urls(url):
    response = requests.get(url, headers=HEADERS)
    text = response.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//table[@class='tbspan']//a/@href")
    detail_urls = map(lambda url:BASE_DOMAIN+url,detail_urls)
    return detail_urls

def parse_detail_page(url):
    movie = {}
    response = requests.get(url,headers=HEADERS)
    text = response.content.decode('gbk')
    html = etree.HTML(text)
    title = html.xpath("//div[@class='title_all']//font["
                       "@color='#07519a']/text()")[0]
    movie['title'] = title

    zoomE = html.xpath("//div[@id='Zoom']")[0]
    imgs = zoomE.xpath(".//img/@src")
    cover = imgs[0]
#    screenshot= imgs[1]
    movie['cover'] = cover
#    movie['screenshot'] = screenshot

    def parse_info(info,rule):
        return info.replace(rule,"").strip()

    infos = zoomE.xpath(".//text()")
    for index,info in enumerate(infos):
        if info.startswith("◎年　　代"):
            info = parse_info(info,"◎年　　代")
            movie['year'] = info
        elif info.startswith("◎简　　介"):
            info = parse_info(info,"◎简　　介")
            for x in range(index+1,len(infos)):
                profile = infos[x].strip()
                movie["profile"] = profile
    download_url = html.xpath("//td[@bgcolor='#fdfddf']/a/@href")[0]
    movie['download_url'] = download_url
    return movie

def spider():
    base_url = "https://www.ygdy8.net/html/gndy/dyzz/list_23_{}.html"
    movies = []
    for x in range(2,3):
        url = base_url.format(x)
        detail_urls = get_detail_urls(url)
        for detail_url in detail_urls:
            movie = parse_detail_page(detail_url)
            movies.append(movie)
            print(movie)

if __name__ == '__main__':
    spider()
