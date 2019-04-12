#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   User.py
@Time    :   2019/04/12 16:52:31
@Author  :   jiegemena 
@Version :   1.0
@Contact :   jiegemena@outlook.com
@License :   https://github.com/jiegemena
@Desc    :   None
'''

# here put the import lib


class User:

    def __init__(self):
        self.id = ''
        self.username = ''
        self.password = ''
        self.truename = ''
        self.state = ''
        self.address = ''
        self.created = ''


if __name__ == '__main__':
    u = User()
    u.id = 'asdffa'

    print(u.id)
