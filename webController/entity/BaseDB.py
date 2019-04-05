# -*- coding: utf-8 -*-
"""
    author: jiege
    url: http://jieguone.top
    copyright: © jieguone.top
    license: none
    date : 2019/4/5 21:53
    ide : PyCharm
"""
from commons.Exception import OutException
from dbcontent import db_sqlite3


class BaseDB:

    def __init__(self, tableName, dbconn):
        self.db = db_sqlite3(sql_conn_str=dbconn)
        self.tableName = tableName

    def add(self, obj):
        sql = "INSERT INTO User "
        par = []
        bval = '('
        eval = '('
        for key in obj:
            bval = bval + str(key) + ','
            eval = eval + '?,'
            par.append(obj[key])

        bval = bval[0:-1] + ')'
        eval = eval[0:-1] + ') '
        sql = sql + bval + ' VALUES ' + eval
        bak = self.db.exec(sql_str=sql, sql_par=par)
        return bak

    def delById(self, id):
        if id <= 0:
            raise OutException('id <= 0,')
        sql = 'DELETE FROM "' + self.tableName + '" WHERE id = ?'
        par = [id]

        bak = self.db.exec(sql_str=sql, sql_par=par)
        return bak

    def findById(self, id):
        if id <= 0:
            raise OutException('id <= 0,')
        sql = 'SELECT * FROM "' + self.tableName + '" where id = ?'
        par = [id]

        bak = self.db.query(sql_str=sql, sql_par=par).fetchone()
        return bak
