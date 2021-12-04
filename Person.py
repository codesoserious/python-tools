# -*- coding: utf-8 -*-

"""
@author: 1
@software: PyCharm
@file: Person.py
@time: 2021/11/7 23:52 
"""


class Person(object):

    def __init__(self, name, age=19):
        self.name = name
        self.__age = age

    def age(self):
        pass

    def set_age(self, param):
        pass


def age(self):
    return self.__age


def set_age(self, age):
    self.__age = age


