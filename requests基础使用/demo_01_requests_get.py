# coding=utf-8

import requests

# 不带参的get请求
response_01 = requests.get(url="http://192.168.5.99:8080/cms")
print(response_01.text) # 响应体
# print(response_01.url)


# 带参数的get请求
parameters = {
    "userAccount": "admin",
    "loginPwd": "123456"
}
response_02 = requests.get(
    url="http://192.168.5.99:8080/cms/manage/loginJump.do",
    params=parameters
)
# print(response_02.text)

