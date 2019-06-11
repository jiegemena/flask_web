from .consultools import register, unregister
from .db_sqlite3 import db_sqlite3

import json
import jgpycshare.LogTools
import jgpycshare.JsonTools
import jgpycshare.DateTime
from flask import session, redirect
from functools import wraps
import uuid

class ILogTools:
    def __init__(self, log):
        self.log = log

    def info(self,str):
        self.log.info(str)

    def error(self,str):
        self.log.error(str)

    def fatal(self,str):
        self.log.exception(str)

    def debug(self,str):
        self.log.debug(str)

def qxlog():
    log = ILogTools(jgpycshare.LogTools.LogTools.get_logger('web', 'info'))
    # log = jgpycshare.LogTools.LogTools.get_logger('web', 'info')
    return log


class CApiRequest:
    """
    - par:
        - request httprequest
            - method
            - sign
            - data
            - appid
            - timestamp int 
            - guid
    """
    def __init__(self, request):
        self.method = request_post(request, 'method')
        if self.method is None:
            raise Exception('method is null')
        self.sign = request_post(request, 'sign')
        if self.sign is None:
            raise Exception('sign is null')
        self.data = request_post(request, 'data')
        if self.data is None:
            pass
        self.timestamp = request_post(request, 'timestamp')
        if self.timestamp is None:
            raise Exception('timestamp is null')
        self.appid = request_post(request, 'appid')
        if self.appid is None:
            raise Exception('appid is null')
        self.guid = request_post(request, 'guid')
        if self.guid is None:
            raise Exception('guid is null')


def apibakjson(code=0, data=None, msg='error', appid=None, key=None, datatype='json'):
    """

    :param code : 10000	接口调用成功，调用结果请参考具体的API文档所对应的业务返回参数
    :param data:
    :param msg:
    :param appid:
    :param key:
    :param datatype:
    :return:
    """
    bakJson = {}
    bakJson['code'] = code
    bakJson['msg'] = msg
    bakJson['appid'] = appid
    bakJson['datatype'] = datatype
    bakJson['timestamp'] = str(jgpycshare.DateTime.DateTime().Now().thisDate)
    bakJson['data'] = data
    bakJson['sign'] = 'sign'
    bakJson['ranstr'] = str(uuid.uuid1())
    return jgpycshare.JsonTools.arraytojson(bakJson)



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
