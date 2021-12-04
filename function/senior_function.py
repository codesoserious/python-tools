# -*- coding: utf-8 -*-

"""
高级函数练习
@author: Andrew
@software: PyCharm
@file: senior_function.py
@time: 2021/11/27 11:53 
"""

''':param 字符串集合'''


def list_element2int(list_str):
    return int(list_str)


str_list = ['12121', '1212121', '121212121']
print(list(map(list_element2int, str_list)))
