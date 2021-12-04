# -*- coding: utf-8 \

"""
@author: Andrew
@software: PyCharm
@file: od_init_01.py
@time: 2021/11/28 20:43 
"""

# unittest测试框架
# 1123454567890-
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

import requests
from logger import logger

# 定义全局变量
init = 'S0'


class Test01(unittest.TestCase):

    # 用于测试用例执行前的初始化工作
    def setUp(self):
        print("test start")

    def test_init(self):
        # testcase()
        global init
        init = "ss"
        logger.info("test_init")

    def test_second(self):
        logger.info('start sleep 5 seconds')
        time.sleep(5)
        logger.info('end sleep 5 second真的是有伊莎润之鸥过后的见哦按别的是多么的爽private String jiajsdiahaijjiasduiadhua ajawiawpadsajidajisdnmisaia iasdjiajdiasjd iasjdihauidjoajhiajdiasuidhasjkdoasjdhausdhaujshjdiasjdiasjdiajiashdahdiuashjduashdihjqwuijhwijaisjdiasjdiasndoaweklqpajdoamdiasjodakjifhasjiahdusandjjaiodjkosjuiandkajkdoashgasoaosdkaodn ')
        self.assertEqual(init, 'SO')


def tearDown(self):
    print("test end")


if __name__ == '__main__':
    init = {'asss': 'sss'}
    # addHeader = {'112':'1212'}
    # 听起来是不错的
    init['key'] = 'asdas'
    # kubectl get pod -n mpaas -o wide
    suite = unittest.TestSuite()
    suite.addTest(Test01("test_init"))
    unittest.defaultTestLoader.discover('')
    #
    # 今天的任务就是完成昨天没有改完的DTS单
    # 生成当前时间字符串,时间格式为:%Y-%m-%d %H-%M-%S
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    # 定义报告存放路径
    filename = os.getcwd() + now + 'result.html'
    print('fileName' + filename)
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp, title='OD测试用例报告', description='用例执行情况:')
    runner.run(suite)
    fp.close()  # 关闭报告
