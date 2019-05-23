#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Entity.py
@Time    :   2019/04/12 16:56:33
@Author  :   jiegemena 
@Version :   1.0
@Contact :   jiegemena@outlook.com
@License :   https://github.com/jiegemena
@Desc    :   None
'''

# here put the import lib
import webCore.db_sqlite3
import webCore.Tools
import config

class Entity:
    def __init__(self,tableName, dbconn=None):
        if dbconn is None:
            dbconn = config.SQL_CONN
        self.db = webCore.db_sqlite3.db_sqlite3(sql_conn_str=dbconn)
        self.tableName = tableName

     # 开启事务
    def setDoWork(self):
        self.db.setDoWork()

    def commitWork(self):
        self.db.commitWork()

    def backWork(self):
        self.db.backWork()

    def exec(self,sql_str, sql_par=()):
        return self.db.exec(sql_str,sql_par)

    def query_all(self, sql_str, sql_par=()):
        cur = self.query(sql_str=sql_str, sql_par=sql_par)
        que = cur.fetchall()
        cols = cur.description
        tmp = []
        for v in que:
            row = {}
            for v2 in range(0, len(cols)):
                row[cols[v2][0]] = v[v2]
            tmp.append(row)
        return tmp

    def query_one(self, sql_str, sql_par=()):
        cur = self.query(sql_str=sql_str, sql_par=sql_par)
        que = cur.fetchone()
        if que is None:
            return None
        cols = cur.description
        row = {}
        for v2 in range(0, len(cols)):
            row[cols[v2][0]] = que[v2]
        return row

    def query(self, sql_str, sql_par=()):
        return self.db.query(sql_str, sql_par)

    def add(self, obj):
        sql = "INSERT INTO `"+ self.tableName +"` "
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
            raise webCore.Tools.OutException('id <= 0,')
        sql = 'DELETE FROM `' + self.tableName + '` WHERE id = ?'
        par = [id]

        bak = self.db.exec(sql_str=sql, sql_par=par)
        return bak

    def findById(self, id):
        if id <= 0:
            raise webCore.Tools.OutException('id <= 0,')
        sql = 'SELECT * FROM `' + self.tableName + '` where id = ?'
        par = [id]

        bak = self.query_one(sql_str=sql, sql_par=par)
        return bak