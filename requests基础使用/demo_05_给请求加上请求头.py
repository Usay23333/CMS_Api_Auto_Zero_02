# coding=utf-8

import requests

'''
知乎如果不加上相应的请求头就会返回400，所以这边我们以知乎为例
'''

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}

response_05 = requests.get("https://zhuanlan.zhihu.com/p/25711916", headers=headers)
print("本次我们实现如何模拟登陆知乎。" in response_05.text)
print(response_05.text)