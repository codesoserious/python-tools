# -*- coding: utf-8 -*-

"""
@author: Andrew
@software: PyCharm
@file: test_init.py
@time: 2021/11/29 21:38 
"""
import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import time

from allure_commons.utils import now

if __name__ == '__main__':
    suits = unittest.defaultTestLoader.discover('odtest/', pattern='od*.py')
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = 'init_test_result.html'
    print('fileName' + filename)
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title='OD测试用例报告', description='用例执行情况:')
    runner.run(suits)
    fp.close()
    pass
