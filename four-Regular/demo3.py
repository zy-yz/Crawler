# encoding: utf-8

import re

# ^（脱字号）
# 在[] 就是取反
# text = "hello"
# ret = re.search('^h',text)
# print(ret.group())

# $，表示已...结尾
# text = "xxx.@163.com"
# ret = re.match('\w+@163.com$',text)
# print(ret.group())

# 贪婪模式和非贪婪模式
# text = "0123456"
# ret = re.match('\d+?',text)
# print(ret.group())
#
# text = "<h1>标题</h1>"
# ret = re.match('<.+>',text)
# print(ret.group())


# 匹配0-100之间的数字
# text = "100"
# ret = re.match('[0-9]\d?$|100$',text)
# print(ret.group())
#
# # r = raw =原生的
# text ='\n'
# print(text)
#
# text = "\\n"
# ret = re.match('\\\\n',text)
# print(ret.group())

# split 函数
text = "helloworld ni hao"
ret = re.split(' ',text)
print(ret)