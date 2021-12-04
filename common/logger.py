# -*- coding: utf-8 -*-

"""
@author: Andrew
@software: PyCharm
@file: logger.py
@time: 2021/12/1 23:15 
"""
import json

from logger import logger


def printStr(msg, args):
    logger.info('*' * 20 + msg + '*' * 20)
    logger.info(' msg=' + args)


def printJson(msg, dictStr):
    logger.info('*' * 20 + msg + '*' * 20)
    logger.info(msg, json.dumps(dictStr))
