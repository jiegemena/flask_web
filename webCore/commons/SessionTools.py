# -*- coding: utf-8 -*-
"""
    author: jiege
    url: http://jieguone.top
    copyright: © jieguone.top
    license: none
    date : 2019/3/31 18:25
    ide : PyCharm
"""
from flask import session


class Session:
    @staticmethod
    def get_session(key):
        try:
            return session.get(key)
        except Exception as e:
            print('db_sqlite3.exec:', e)
            return None

    @staticmethod
    def set_session(key, val):
        session[key] = val

