# coding=utf-8

import requests

res = requests.get("https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png", verify=False)
print(res.content) # 获取响应体的字节形式

fp = open("test.png", mode='wb')
fp.write(res.content)
fp.close()