# coding=utf-8

import pymysql

db = pymysql.Connect(
    host="192.168.5.99",
    port=3306,
    user="root",
    password="123456",
    database="cms",
    charset='utf8',
)
cur = db.cursor() # 获取游标
print(cur.execute("select user_account from sys_user;"))

print(cur.fetchone()) # 从游标中取出单条数据
print(cur.fetchone())
print(cur.fetchall()) # 从游标中取出所有数据

cur.close() # 关闭游标
db.close() # 关闭数据库连接