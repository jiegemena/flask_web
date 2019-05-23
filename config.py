DEBUG = True
PORT = 8080
HOST = '127.0.0.1'
WEBNAME='jgcloudd'
SECRET_KEY = 'web'

# 提交参数拦截
REQUEST_INTERCEPT = "'| and| exec| union| create| insert| select| delete| update| count| * | chr| mid| master| truncate| char| declare| xp| or|--"
SESSION_KEY_PREFIX = 'dome'

#log 文件
LOGPATH = 'logs'

# sqlite 文件
SQL_CONN = 'appdata/web.db'
SQL_INIT = 'appdata/init.sql'