# -*- coding: utf-8 -*-
import requests as request

"""
@author: Andrew
@software: PyCharm
@file: spider.py
@time: 2021/11/19 22:10 
"""

if __name__ == '__main__':
    resp = request.get('https://www.baidu.com')
    if resp.status_code != 200:
        pass
    elif resp.status_code == 404:
        print("网页地址找不到")
    else:
        print(type(resp.status_code))
        print(f"百度请求状态码:{resp.status_code}%s", resp.status_code)
        print(resp.content)
