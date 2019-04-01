# -*- coding: utf-8 -*-
"""
    :author: jiegemena
    :url: http://jieguone.top
    :copyright: © jieguone.top
    :license: none
    :20190331
"""
from webController.entity.UserRepository import UserRepository


class UserService:

    def __init__(self, current_app):
        self.UserRepository = UserRepository(current_app.config['SQL_CONN'])

    def findall(self):
        return self.UserRepository.findall()