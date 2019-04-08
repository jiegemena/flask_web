# -*- coding: utf-8 -*-
from flask import Blueprint, request, current_app, render_template

from webController.blueprints.admincontroller.Login import Login
from webController.tools.requirLogin import requirLogin
from webCore.commons.Exception import OutException

admin_bp = Blueprint('admin', __name__, template_folder="templates", static_url_path='', static_folder='static')


@admin_bp.after_request
def after_request(response):
    # token = 'print_request_info'
    # response.set_cookie('print_request_info', token)
    # print('request end')
    return response


@admin_bp.before_request
def print_request_info():
    print("请求地址：print_request_info" + str(request.path))

    # print("请求地址：" + str(request.path))
    # print("请求方法：" + str(request.method))
    # print("---请求headers--start--")
    # print(str(request.headers).rstrip())
    # print("---请求headers--end----")
    # print("GET参数：" + str(request.args))
    # print("POST参数：" + str(request.form))


@admin_bp.route('/home/<action>', methods=['GET', 'POST'])
@requirLogin
def home(action):
    if action == 'index':
        current_app.config['log'].info('enter admin')
        return render_template('home/index.html')
    else:
        raise OutException('no action')


@admin_bp.route('/login/<action>', methods=['GET', 'POST'])
def login(action):
    if action == 'index':
        return render_template('login/login.html')
    elif action == 'in':
        user = request.form['username']
        passw = request.form['password']
        login = Login(current_app.config['SQL_CONN'])
        return login.In(user, passw)
    else:
        raise OutException('no action')


@admin_bp.route('/user/<action>', methods=['GET', 'POST'])
def user(action):
    if action == 'index':
        return render_template('user/index.html')
    else:
        raise OutException('no action')

