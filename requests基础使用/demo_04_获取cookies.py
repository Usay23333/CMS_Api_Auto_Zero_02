# coding=utf-8

import requests

login_data = {
    "userAccount": "admin",
    "loginPwd": "123456"
}
response = requests.post("http://192.168.5.99:8080/cms/manage/loginJump.do", data=login_data)

# print(response.text)
print(response.cookies)


query_user_data = {
    "startCreateDate": "",
    "endCreateDate": "",
    "searchValue": "admin",
    "page": "1"
}
response_02 = requests.post("http://192.168.5.99:8080/cms/manage/queryUserList.do", data=query_user_data, cookies=response.cookies)
print(response_02.text)

