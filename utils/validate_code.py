# -*- coding: utf-8 -*-

"""
@author: Andrew
@software: PyCharm
@file: validate_code.py
@time: 2021/11/27 20:36 
"""
import string
import random
from itertools import groupby
from operator import itemgetter

number = '0123456789'
all_letters = string.ascii_letters


def get_digit_code(digit):
    # global number
    combination = number + all_letters
    # 判断位数是不是Int的
    if isinstance(digit, int):
        # 返回随机的6个字符的验证码
        return ''.join(random.sample(combination, digit))
    else:
        raise ValueError('this digit is not int')


# 对list里的元素按照某个字段进行分组的需求的话，可以通过itertools模块中的groupby实现。
def dictvalue_by_itemgetter(field, lists):
    if isinstance(field, str) and len(field) > 0:
        keyGet = itemgetter(field)
        return list(map(lambda entity: keyGet(entity), lists))
    else:
        raise TypeError('this dict key is not String')


def group_by_field(field, lists):
    return list(dict)


if __name__ == '__main__':
    with open('/home/mpaas/log/auto.log', 'a+') as logfile:
        logfile.write(get_digit_code(6) + '\n')
    # print()
    srs = [{'key': 121221}, {'key': 121221}, {'key': 1255}]
    print(dictvalue_by_itemgetter('key', srs))
    key_get = itemgetter('key')
    for key in srs:
        print(key_get(key))
    for keys, val in groupby(srs, key=itemgetter('key')):
        print(keys)
        print(list(val))
    print(list(groupby(srs, key=itemgetter('key'))))
    # render_template('response.html', result=srs)
    # srs.sort(reverse=True)
    # for x in groupby(srs, key=itemgetter()):
    #     print(x)
