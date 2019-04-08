# -*- coding: utf-8 -*-
"""
    author: jiege
    url: http://jieguone.top
    copyright: © jieguone.top
    license: none
    date : 2019/4/6 0:01
    ide : PyCharm
"""
from webCore.commons.SessionTools import Session
from flask import redirect


def requirLogin(func):
    def do(*args, **kwargs):
        Login = Session.get_session('Login')
        if Login == 'login':
            return func(*args, **kwargs)
        else:
            return redirect('/admin/login/index')
    return do
