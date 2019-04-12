# here put the import lib
from flask import Blueprint, request, current_app, render_template, redirect
import webCore.Tools

api_bp = Blueprint('api', __name__, template_folder="templates",
                   static_url_path='', static_folder='static')

@api_bp.after_request
def after_request(response):
    return response

@api_bp.before_request
def print_request_info():
    pass
    # print("api_bp.before_request-请求地址：print_request_info:" + str(request.path))
    # for key in request.form:
    #         print("api_bp.before_request-key：{}   value：{}".format(key, request.form[key]))


@api_bp.route('/home/<action>', methods=['GET', 'POST'])
def home(action):
    return webCore.Tools.apibakjson()