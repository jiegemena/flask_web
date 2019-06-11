#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   guest.py
@Time    :   2019/04/12 17:47:35
@Author  :   jiegemena 
@Version :   1.0
@Contact :   jiegemena@outlook.com
@License :   https://github.com/jiegemena
@Desc    :   None
'''


# here put the import lib
from flask import Blueprint, request, current_app, render_template, redirect, make_response
import uuid
import entity.Entity
import jgpycshare.StringTools
import tools

guest_bp = Blueprint('guest', __name__, template_folder="templates",
                   static_url_path='', static_folder='static')

@guest_bp.after_request
def after_request(response):
    return response

@guest_bp.before_request
def print_request_info():
    pass
    # print("GET参数：" + str(request.args))
    # print("POST参数：" + str(request.form))

@guest_bp.route('/home', methods=['GET', 'POST'])
def home():
    cookie = request.cookies.get(current_app.config['WEBNAME']) 
    return tools.apibakjson(data=cookie)


@guest_bp.route('/', methods=['GET', 'POST'])
def index():
    return redirect('/ui/index')
    # resp = make_response(render_template('index.html'))
    # gio = str(uuid.uuid1())
    # resp.set_cookie(current_app.config['WEBNAME'], gio)
    # return resp

@guest_bp.route('/api/<action>', methods=['GET', 'POST'])
def api(action):

    if action == 'login':
        username = tools.request_post(request, 'username')
        pwd = tools.request_post(request, 'pwd')

        pwd = jgpycshare.StringTools.StringTools.get_login_pass(pwd)

        sqlstr = 'SELECT * FROM `jguser` where username = ? and password = ?'
        sqlpar = []
        sqlpar.append(username)
        sqlpar.append(pwd)

        userentity = entity.Entity.Entity('jguser')
        user = userentity.query_one(sqlstr, sqlpar)
        print(user)
        if user is None:
            return tools.apibakjson(code=0,data='',msg='errorlogin')

        sqlstr = "UPDATE `jguser` SET `loginguid` = ? WHERE id = " + str(user['id'])
        sqlpar = []
        sqlpar.append(str(uuid.uuid1()))
        userentity.exec(sqlstr, sqlpar)

        user = userentity.findById(user['id'])
        if user is None:
            return tools.apibakjson(code=0,data='',msg='errorlogin')
        print(user)
        
        user['password'] = ''
        return tools.apibakjson(code=1,data=user,msg='success')
        # resp = make_response(redirect('/ui/index'))
        # gio = str(uuid.uuid1())
        # resp.set_cookie(current_app.config['WEBNAME'], gio)
        # return resp

    return 'welcome web api!'


@guest_bp.route('/ui/<action>', methods=['GET', 'POST'])
def ui(action):
    if action == 'index':
        # resp = make_response(render_template('index.html'))
        # gio = str(uuid.uuid1())
        # resp.set_cookie(current_app.config['WEBNAME'], gio)
        return render_template('index.html')
    if action == 'login':
        return render_template('login.html')
    return 'welcome web demo!'