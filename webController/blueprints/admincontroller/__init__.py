# -*- coding: utf-8 -*-
from flask import Blueprint, request, current_app, render_template

admin_bp = Blueprint('admin', __name__, template_folder="templates", static_url_path='', static_folder='static')


@admin_bp.after_request
def after_request(response):
    token = 'print_request_info'
    response.set_cookie('print_request_info', token)
    print('request end')
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
def index():
    current_app.config['log'].info('enter admin')
    return render_template('login.html')
