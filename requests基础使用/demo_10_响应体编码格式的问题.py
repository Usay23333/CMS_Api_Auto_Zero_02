# coding=utf-8

import requests

response_01 = requests.post(url="http://192.168.5.99:8080/cms", timeout=10)

# 1.智能判断
response_01.encoding = response_01.apparent_encoding

# 2.指定编码格式
# response_01.encoding = "UTF-8"

print(response_01.text)