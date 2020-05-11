# encoding= utf-8

import pymysql

conn = pymysql.connect(host='121.196.205.196',user='root',password='123456',database='mydb',port=3306)

cursor = conn.cursor()

cursor.execute("select * from user1")
result = cursor.fetchone()
print(result)

conn.close()