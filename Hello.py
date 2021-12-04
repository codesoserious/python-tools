import math
import os
from decimal import Decimal

from ListType import ListType
from WeekEnum import WeekEnum
from table import customer_table as ct, customer_table

init = "aa"
print(f"hello world {init}")
# 演示字符串转义
""" 注释:
这个是第一个python文件
"""
print(
    f"""
11111 {init}
11111
"""
)
print(f"\\ 100 \" '")

ss = ListType()
dec = Decimal()


def to_list(str):
    if str == '1234':
        return str + "ok"


ids = '1234,12121,1212'
listsr = map(to_list, ids.split(','))
print(filter(None, list(listsr)))

ct.loop_method()


# ss.name = "111"
# print(ss.name)


def lis():
    return 11, 222


def power(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    result = 1
    while n > 0:
        n = n - 1
        result = x * result
    while n < 0:
        return result


# print(lis())
# 计算x的n次方
# print(power(2, 1))
print(math.pow(2, -1))
print(WeekEnum.FRIDAY.value)
string = "12121"
if isinstance(string, str):
    print(f"{string}前三位是" + string[:3])
input('Press Enter to exit…')
customer_table.loop_method()
