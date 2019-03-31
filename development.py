

DEBUG = True
PORT = 8080
HOST = '127.0.0.1'

# 提交参数拦截
REQUEST_INTERCEPT = "'|and|exec|union|create|insert|select|delete|update|count|*|chr|mid|master|truncate|char|declare|xp|or|--"
SESSION_KEY_PREFIX = 'dome'

# sqlite 文件
SQL_CONN = 'db/web.db'
SQL_INIT = 'db/init.sql'