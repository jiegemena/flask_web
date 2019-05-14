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
from flask import Blueprint, request, current_app, render_template, redirect
import webCore.Tools

guest_bp = Blueprint('guest', __name__, template_folder="templates",
                   static_url_path='', static_folder='static')

@guest_bp.after_request
def after_request(response):
    return response

@guest_bp.before_request
def print_request_info():
    pass
    # print("api_bp.before_request-请求地址：print_request_info:" + str(request.path))
    # for key in request.form:
    #         print("api_bp.before_request-key：{}   value：{}".format(key, request.form[key]))


@guest_bp.route('/home/<action>', methods=['GET', 'POST'])
def home(action):
    return webCore.Tools.apibakjson()

@guest_bp.route('/', methods=['GET', 'POST'])
def index():
    return 'welcome web demo!'