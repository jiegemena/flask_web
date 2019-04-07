# -*- coding: utf-8 -*-
"""
    author: jiege
    url: http://jieguone.top
    copyright: © jieguone.top
    license: none
    date : 2019/3/31 15:46
    ide : PyCharm
"""
from flask import Blueprint, current_app
from webController.services.UserService import UserService
from webCore.commons.SessionTools import Session

web_bp = Blueprint('web', __name__, template_folder="templates", static_url_path='', static_folder='static')


@web_bp.route('/')
def index():
    username = Session.get_session('username')
    if username is None:
        username = ''
    # blog_bp.config['log'].info('enter admin')

    # dbuser = UserService(current_app=current_app)
    #     # u = dbuser.findall()
    # print(u)
    return 'hello index:' + username


@web_bp.route('/login')
def login():
    # username = request.form.get('username')
    Session.set_session('username', 'jiegemena')
    # blog_bp.config['log'].info('enter admin')
    return 'hello index'
