# encoding= utf-8

import pymongo

#   获取连接mongodb的对象
client = pymongo.MongoClient('121.196.205.196',port=27017)

# 获取数据库
db = client.qq

# 获取数据库中的集合(也就是MySQL中的表)
collection = db.qa

# 写入数据
# collection.insert({"username":"aaa"})
# collection.insert_many({
#     "username":"aaa",
#     'age': 18
# })

# 获取集合中的一条数据
result = collection.find_one({"username":"aaa"})
print(result)

# 更新数据
collection.update_one({"username":"aaa"},{"$set":{"username":"ccc"}})
collection.update_many({"username":"aaa"},{"$set":{"username":"ccc"}})