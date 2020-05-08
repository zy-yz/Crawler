
import requests
from lxml import etree


# 1.将目标网站上的页面抓取下来
headers ={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
}

url = 'https://movie.douban.com/cinema/nowplaying/chengdu/'
response = requests.get(url,headers=headers)
text = response.text
# print(text)
#   reponse.text返回的是一个经过解码后的字符串，是str(unicode)类型
#   response.content:返回的时候一个原生字符串，就是从网页上抓取下来，没有经过处理的字符串

# 2.将抓取下来的数据按一定规则提取
html = etree.HTML(text)
ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(ul,encoding='utf-8').decode("utf-8"))
lis = ul.xpath("./li")
movies = []
for li in lis:
    title = li.xpath("@data-title")[0]
    thunbnail = li.xpath(".//img/@src")[0]
    movie = {
        'title',title,
        'thunbnail',thunbnail

    }
    movies.append(movie)
print(movies)