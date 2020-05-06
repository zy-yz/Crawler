from urllib import parse

url ='http://www.baidu.com/s?wd=python'

result = parse.urlparse(url)
result1 = parse.urlsplit(url)
print(result)
print(result1)
#其实是一样的，只是urlparse对了一个字段params，但这个字段基本没用
# ParseResult(scheme='http', netloc='www.baidu.com', path='/s', params='', query='wd=python', fragment='')
# SplitResult(scheme='http', netloc='www.baidu.com', path='/s', query='wd=python', fragment='')
print(result.scheme)