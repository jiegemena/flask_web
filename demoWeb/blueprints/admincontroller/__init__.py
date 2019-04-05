# -*- coding: utf-8 -*-
from flask import Blueprint, request, current_app, render_template, redirect

from commons import Session
from demoWeb.services.UserService import UserService
from demoWeb.tools.requirLogin import requirLogin

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


@admin_bp.route('/')
@requirLogin
def index():
    current_app.config['log'].info('enter admin')

    return render_template('index.html')


@admin_bp.route('/login')
def login():

    return render_template('login.html')


@admin_bp.route('/loginIn')
def loginIn():
    user = request.args['username']
    passw = request.args['password']
    userService = UserService(SQL_CONN=current_app.config['SQL_CONN'])
    userS = userService.checkLoginUser(user, passw)
    if userS is None:
        return redirect('/admin/login')

    Session.set_session('LoginUser', userS)
    Session.set_session('Login', 'login')
    return redirect('/admin')
