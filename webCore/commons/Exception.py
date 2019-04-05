# -*- coding: utf-8 -*-
"""
    author: jiege
    url: http://jieguone.top
    copyright: © jieguone.top
    license: none
    date : 2019/4/5 21:49
    ide : PyCharm
"""


# 通过继承Exception或者BaseException类实现自定义异常类
class OutException(BaseException):
    def __init__(self, mesg="throw a Exception"):
        print(mesg)
