# -*- coding: utf-8 -*-

"""
@author: Andrew
@software: PyCharm
@file: http_rquest.py
@time: 2021/12/1 23:12 
"""
import json

import requests

from common import logger


def post(url=None, data=None, headers=None):
    logger.printStr('url', url)
    requests.post(url, data=json.dumps(data), headers=headers)
