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

try:
    cur.execute("update user set blance = blance - 100 where name = 'zero';")
    cur.execute("update user set blance = blance + 100 where name = 'lisi';")
    db.commit() # 提交
except:
    db.rollback() # 回滚

cur.close() # 关闭游标
db.close() # 关闭数据库连接