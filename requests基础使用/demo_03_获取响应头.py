# coding=utf-8

import requests

login_data = {
    "userAccount": "admin",
    "loginPwd": "123456"
}
response = requests.post("http://192.168.5.99:8080/cms/manage/loginJump.do", data=login_data)

# print(response.text)
print(type(response.headers))
print(response.headers['Set-Cookie'].split(";")[0])