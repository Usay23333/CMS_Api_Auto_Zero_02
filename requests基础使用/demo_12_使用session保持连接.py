# coding=utf-8

import requests

s = requests.Session()

login_data = {
    "userAccount": "admin",
    "loginPwd": "123456"
}
response = s.post(
    "http://192.168.5.99:8080/cms/manage/loginJump.do",
    data=login_data
)
print(response.json()["msg"])


query_user_data = {
    "startCreateDate": "",
    "endCreateDate": "",
    "searchValue": "admin",
    "page": "1"
}
response_02 = s.post(
    "http://192.168.5.99:8080/cms/manage/queryUserList.do",
    data=query_user_data,
)
print(response_02.text)