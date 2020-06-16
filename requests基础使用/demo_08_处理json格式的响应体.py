# coding=utf-8

import requests
import json

login_data = {
    "userAccount": "admin",
    "loginPwd": "123456"
}
response_02 = requests.post(
    url="http://192.168.5.99:8080/cms/manage/loginJump.do",
    data=login_data
)
print(response_02.text)

# 第一种方法：使用json模块将json字符串转成python字典
# res_dict = json.loads(response_02.text)
# print(res_dict["msg"])
# print(type(login_data))

# 第二种方法：requests本身提供的json()方法，前提是响应体是json格式
print(response_02.json()["msg"])
print(type(response_02.json()))