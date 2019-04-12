# -*- coding: utf-8 -*-
"""
    :author: jiegemena
    :url: http://jieguone.top
    :copyright: © jieguone.top
    :license: none
"""
import sqlite3


class db_sqlite3:

    def __init__(self, sql_conn_str):
        print('''conn database''')
        self.conn = sqlite3.connect(sql_conn_str)
        self.cursor = None
        self.total_changes = 0
        self.dowork = False

    # 开启事务
    def setDoWork(self):
        print('db_sqlite3.setDoWork')
        self.dowork = True

    def commitWork(self):
        print('db_sqlite3.commitWork')
        self.conn.commit()

    def backWork(self):
        print('db_sqlite3.backWork')
        self.conn.rollback()

    def __del__(self):
        self.close()

    def exec(self, sql_str, sql_par=()):
        print(sql_str)
        print(sql_par )
        try:
            self.get_db().execute(sql_str, sql_par)
            if self.dowork is False:
                print('exec.commit')
                self.conn.commit()
                # 返回影响数
                changes = self.conn.total_changes
                cha = changes - self.total_changes
                self.total_changes = changes
                return cha
            else:
                return 1
        except Exception as e:
            if self.dowork is False:
                self.conn.rollback()
            print('db_sqlite3.exec:', e)
            raise e

    def query(self, sql_str, sql_par=()):
        print(sql_str)
        print(sql_par)
        return self.get_db().execute(sql_str, sql_par)

    def get_db(self):
        if self.cursor is None:
            self.cursor = self.conn.cursor()
        return self.cursor

    def close(self):
        self.cursor = None
        self.conn.close()
        print('''close database''')

