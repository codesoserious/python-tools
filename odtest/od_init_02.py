# -*- coding: utf-8 -*-

"""
@author: Andrew
@software: PyCharm
@file: od_init_01.py
@time: 2021/11/28 20:43 
"""

# unittest测试框架
import unittest

from logger import logger

from odtest.od_init_01 import init


class Test02(unittest.TestCase):
    global secnod

    # 用于测试用例执行前的初始化工作
    def setUp(self):
        print("test start")
        logger.info(init)

    def test_init(self):
        logger.info("start test init")
        stop = 'true'
        self.assertEqual(init, 'S1')
        self.assertEqual(stop, 'true')
        logger.info('test init end')

    def tearDown(self):
        print("test end")
