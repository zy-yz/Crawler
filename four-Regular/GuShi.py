import requests
import re

def parse_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"
    }

    response = requests.get(url,headers)
    text = response.text
    # print(text)
    titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>',text,re.DOTALL)
    #print(titles)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    # print(dynasties)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>',text,re.DOTALL)
    content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>',text,re.DOTALL)
    print(content_tags)
    contents = []
    for content in content_tags:
        x=re.sub(r'<.*?',"",content)
        contents.append(x.strip())

    poems = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynasty,author,content = value
        poem = {
            'title':title,
            'dynasty':dynasty,
            'author':author,
            'content':content
        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print("==="*12)

def main():
    url = 'https://www.gushiwen.org/default.aspx?page=2'
    for x in range(1,11):
        url = "https://www.gushiwen.org/default.aspx?page=%s" %x
        parse_page(url)
    parse_page(url)
if __name__ == '__main__':
   main()