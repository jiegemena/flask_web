# flask_learn
flask web 框架的学习

### 开始入门 python3.7 flask

#### 按照习惯，开发一个小博客
- web : flask
- templates : Jinja2
- sql : sqlite3
- ide : pycharm
- vcs : git
- wsgi : gunicorn
- public : docker

#### 目录
- db : 存放数据库文件   
1、init.sql : 数据库初始化文件   
2、init.sql.lock : 安装后锁定数据库初始化文件，删除可重置   
3、web.db : sqlite3 db文件   

- Log : 日志文件

- webController : 项目业务文件

- webCore : web核心目录

- app.py : 项目入口文件

- development : 测试环境配置文件

-  Dockerfile : docker build 文件

- gunicorn.conf.py : gunicorn配置文件

- production.py : 生产环境配置文件

- requirements :  项目依赖文件
