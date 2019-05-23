#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Tools.py
@Time    :   2019/04/12 16:37:13
@Author  :   jiegemena 
@Version :   1.0
@Contact :   jiegemena@outlook.com
@License :   https://github.com/jiegemena
@Desc    :   None
'''

# here put the import lib
import json
import jgpycshare.LogTools
import jgpycshare.DateTime
from flask import session, redirect
from functools import wraps


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




def backjson(code=0, data=None, msg='error'):
    bakJson = {}
    bakJson['code'] = code
    bakJson['msg'] = msg
    bakJson['timestamp'] = jgpycshare.DateTime.DateTime().Now().ToString()
    if data is not None:
        bakJson['data'] = data
    return json.dumps(bakJson)

# 通过继承Exception或者BaseException类实现自定义异常类
class OutException(BaseException):
    def __init__(self, mesg="throw a Exception"):
        print(mesg)

def qxlog():
    log = jgpycshare.LogTools.LogTools.get_logger('web', 'info')
    return log

def apibakjson(code=0, data=None, msg='error', merid=None, key=None):
    bakJson = {}
    bakJson['code'] = code
    bakJson['msg'] = msg
    bakJson['merid'] = merid
    bakJson['datatype'] = 'rsa2'
    bakJson['timestamp'] = jgpycshare.DateTime.DateTime().Now().ToString()
    bakJson['data'] = data
    bakJson['ranstr'] = 'ranstr'
    return json.dumps(bakJson)



def request_get(request,key):
    try:
        return request.args[key]
    except Exception as e:
        print(key,'is no none',e)
        return None
    
def request_post(request,key):
    try:
        return request.form[key]
    except Exception as e:
        print(key,'is no none',e)
        return None


def requirLogin(func):
    @wraps(func)
    def do(*args, **kwargs):
        Login = Session.get_session('Login')
        print(Login)
        if Login is not None and len(Login) > 0:
            return func(*args, **kwargs)
        else:
            return apibakjson(code=0,data='',msg='Authentication failure') 
    return do
