# -*- coding: utf-8 -*-
"""
    author: jiege
    url: http://jieguone.top
    copyright: © jieguone.top
    license: none
    date : 2019/4/4 21:21
    ide : PyCharm
"""
from webCore.commons.SessionTools import Session
from webController.services.UserService import UserService


class Login:
    def __init__(self, SQL_CONN):
        self.SQL_CONN = SQL_CONN

    def In(self, user, pass_w):
        if len(user) <= 1 or len(pass_w) <= 1:
            return False
        pass_w = UserService.getLoginPass(pass_w)
        userService = UserService(SQL_CONN=self.SQL_CONN)
        userS = userService.checkLoginUser(user, pass_w)
        if userS is None:
            return 'False'
        Session.set_session('LoginUser', userS)
        Session.set_session('Login', 'login')
        return 'True'
