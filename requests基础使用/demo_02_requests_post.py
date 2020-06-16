# coding=utf-8

import requests

# 不带参数的post请求
response_03 = requests.post(url="http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportProvince")
# print(response_03.text)


# 带参数的post请求
data = {
    "byProvinceName": "黑龙江"
}
response_04 = requests.post(
    url="http://www.webxml.com.cn/WebServices/WeatherWebService.asmx/getSupportCity",
    data=data
)
# print(response_04.text)

