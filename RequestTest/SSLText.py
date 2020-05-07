import  requests

# 对于那些已经信任的ssl的网站，直接使用requests就可以返回正常响应
#   对于不受信任的就需要加verity=false这个参数
resp = requests.get("http://www.baidu.com",verify=False)
print(resp.content.decode('utf-8'))