# -*- coding: utf-8 -*-
"""
    :author: jiegemena
    :url: http://jieguone.top
    :copyright: © jieguone.top
    :license: none
    :20190331
"""
from webController.entity.UserRepository import UserRepository


class UserService:

    def __init__(self, SQL_CONN):
        print(SQL_CONN)
        self.UserRepository = UserRepository(SQL_CONN)
        print(SQL_CONN)

    def findall(self):
        return self.UserRepository.findall()

    def checkLoginUser(self, user, pass_w):
        return self.UserRepository.Query(username=user, password=pass_w).fetchone()


if __name__ == '__main__':
    s = UserService(SQL_CONN='C:\\Users\\jiege\\PycharmProjects\\firstFlask\\db\\web.db')
    print(s.checkLoginUser('jiege','jiege'))