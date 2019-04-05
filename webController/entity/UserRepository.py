# -*- coding: utf-8 -*-
"""
    author: jiege
    url: http://jieguone.top
    copyright: © jieguone.top
    license: none
    date : 2019/3/31 14:42
    ide : PyCharm
"""
from demoWeb.entity.BaseDB import BaseDB
from jgpycshare.DateTime import DateTime


class UserRepository(BaseDB):

    def __init__(self, sql_conn_str=''):
        super(UserRepository, self).__init__(tableName='User', dbconn=sql_conn_str)

    def findall(self):
        return self.db.query('SELECT *  from User ').fetchall()

    def Query(self, username=None, password=None, truename=None, state=None, pageindex=1, pageSize=10):
        sql = 'SELECT * from User where 1=1 '
        par = []
        if username is not None:
            sql = sql + ' and username = ?'
            par.append(username)

        if password is not None:
            sql = sql + ' and password = ?'
            par.append(password)

        if truename is not None:
            sql = sql + ' and truename = ?'
            par.append(truename)

        if state is not None:
            sql = sql + ' and state = ?'
            par.append(state)

        bak = self.db.query(sql_str=sql, sql_par=par)
        return bak


if __name__ == '__main__':
    user = UserRepository(sql_conn_str='C:\\Users\\jiege\\PycharmProjects\\firstFlask\\db\\web.db')
    # print(str(user.delById(3)))
    # print(user.findById(1))
    # print(DateTime.Now())
    # userModel = {'username': 'test1', 'password': 'password', 'truename': 'truename', 'state': 1, 'address': 'address'}
    # i = 5
    # while i > 0:
    #     i = i - 1
    #     user.add(userModel)
    # u = user.Query(username='test2').fetchall()
    # print(u)
    # print(DateTime.Now())
