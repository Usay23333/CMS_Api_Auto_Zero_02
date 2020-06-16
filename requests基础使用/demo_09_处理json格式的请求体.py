# coding=utf-8

import requests
import json

login_url = "http://testgw.whalehouse.com:8080/jc-gateway-outer/api/paiu/rf/login?app_key=APK100010&timestamp=2019-11-20%2021:54:49&sign=C87CDC43EEBA3412DA349153A74AF4BB&sign_type=md5&version=1.0&customerId=RF"
login_data = {
    "deveiceId": "imei-865166010001876",
    "password": "14e1b600b1fd579f47433b88e8d85291",
    "userName": "gx"
}
print(type(login_data))
# 第一种方法：使用json模块将指定数据转换为json字符串
res = requests.post(login_url, data=json.dumps(login_data))
print(res.text)

# 第二种方法：使用requests.post中的关键字参数json接收
res_01 = requests.post(login_url, json=login_data)
print(res_01.text)
