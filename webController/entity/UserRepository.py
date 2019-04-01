# -*- coding: utf-8 -*-
"""
    author: jiege
    url: http://jieguone.top
    copyright: © jieguone.top
    license: none
    date : 2019/3/31 14:42
    ide : PyCharm
"""
from webCore.dbcontent import db_sqlite3


class UserRepository:
    def __init__(self, sql_conn_str=''):
        self.db = db_sqlite3(sql_conn_str=sql_conn_str)

    def findall(self):
        return self.db.query('SELECT *  from User ').fetchall()


