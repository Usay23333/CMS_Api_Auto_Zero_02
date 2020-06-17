# coding=utf-8

import requests
import random

proxies_list = [
    {
    'http': 'http://192.168.5.31:8888',
    'https': 'https://localhost:8888'
    },
    {
    'http': 'http://192.168.5.6:8888',
    'https': 'https://localhost:8888'
    },
    {
    'http': 'http://192.168.5.10:8888',
    'https': 'https://localhost:8888'
    },
]
_proxie = random.choice(proxies_list)
print(_proxie)
response_01 = requests.post(
    url="http://192.168.5.99:8081/cms",
    timeout=10, # 设置请求超时时间
    proxies=_proxie,
)

print(response_01.text[:100])
