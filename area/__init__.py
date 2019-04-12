#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   __init__.py
@Time    :   2019/04/12 17:48:32
@Author  :   jiegemena 
@Version :   1.0
@Contact :   jiegemena@outlook.com
@License :   https://github.com/jiegemena
@Desc    :   None
'''

# here put the import lib
from .admin.admin import admin_bp
from .api.api import api_bp
from .guest.guest import guest_bp