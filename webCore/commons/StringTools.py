# -*- coding: utf-8 -*-
"""
    author: jiege
    url: http://jieguone.top
    copyright: © jieguone.top
    license: none
    date : 2019/3/31 18:33
    ide : PyCharm
"""
import hashlib


class StringTools:
    @staticmethod
    def get_login_pass(value):
        return StringTools.get_md5_utf8('e10adc3949ba59abbe56e057f20f883e' + value)

    @staticmethod
    def get_md5_utf8(value):
        return hashlib.md5(value.encode(encoding='UTF-8')).hexdigest()

