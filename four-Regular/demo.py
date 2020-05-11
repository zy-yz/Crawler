
# encoding: utf-8

import  re


# #1.匹配某个字符串
# text = "hello"
# ret = re.match('he',text)
# print(ret.group())

# 2.匹配任意的字符串,第一个
# text = "4hello"
# ret = re.match('.',text)
# print(ret.group())

# 3 .\d，匹配任意的数字(0-9),也是只有一个
# text= "945"
# ret = re.match('\d',text)
# print(ret.group())

# 4.\D，匹配任意的非数字
# text = "re"
# ret = re.match("\D",text)
# print(ret.group())

# 5.\s匹配空白字符(\n,\t,\r,空格)
# text = "\t"
# ret = re.match('\s',text)
# print(ret.group())

# 6 \w,匹配的是a-z,A-Z,数字和下划线
# text = "_"
# ret = re.match("\w",text)
# print(ret.group())

# 7,\W，与小写的相反
# text = "a"
# ret = re.match('\w',text)
# print(ret.group())

# 8 []组合的方式，只要满足中括号中的字符，就可以匹配
# text = "3434-4343"
# ret = re.match('[\d\-]+',text)
# print(ret.group())

# 前面的集中简单的匹配规则，都可以用[]来替代
# \d [0-9]
# \D [^0-9]
# \w [0-9a-zA-Z_]
# \W [^0-9a-zA-Z_]


# ####匹配多个字符
# 9 *可以匹配0或则任意多个字符
# text = "abcd"
# ret = re.match('.*',text)
# print(ret.group())


# 10,匹配1个或者多个字符
# text= "agcfd"
# ret = re.match('\w+',text)
# print(ret.group())

#11 ? 匹配一个或者0个(妖魔没有，妖魔一个)
# text = "abcd"
# ret = re.match('\w?',text)
# print(ret.group())

# 12 {m},匹配m个字符
text= "abcd"
ret = re.match('\w{2}',text)
print(ret.group())


