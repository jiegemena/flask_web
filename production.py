DEBUG = False
PORT = 80
HOST = '0.0.0.0'

# 提交参数拦截
REQUEST_INTERCEPT = "'|and|exec|union|create|insert|select|delete|update|count|*|chr|mid|master|truncate|char|declare|xp|or|--"
SESSION_KEY_PREFIX = 'dome'

# sqlite 文件
SQL_CONN = 'db/web.db'
SQL_INIT = 'db/init.sql'