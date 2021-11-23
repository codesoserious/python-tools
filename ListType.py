# -*- coding: utf-8 -*-

"""
@author: 1
@software: PyCharm
@file: ListType.py
@time: 2021/11/7 21:49 
"""


class ListType(object):
    __slots__ = '_fileName'

    def __init__(self, fileName=None):
        if fileName is None:
            self._fileName = fileName

    """
    :return fileName
    """
    @property
    def fileName(self):
        return self._fileName

    """:param fileNameq"""
    @fileName.setter
    def fileName(self, fileName):
        pass

    def toString(self):
        return f"fileName={self.fileName}"
