'''
@File    :   public.py
@Time    :   2019/05/20 17:03:52
@Author  :   jiegemena 
@Version :   1.0
@Contact :   jiegemena@outlook.com
@Desc    :   发布项目
'''

# here put the import lib

import os 
import os.path 
import shutil 
import time, datetime

def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path) 
        print(path+' 创建成功')
        return True
    else:
        print(path+' 创建成功')
        return False

def copyfile(oldf,newf):
    shutil.copy(oldf, newf)

def copys(oldf,newf): 
    for root, dirs, files in os.walk(oldf):
        filenametmp = newf + root
        if filenametmp.find('__pycache__') >= 0:
            continue
        mkdir(filenametmp)
        for f in files:
            shutil.copy(root + '/' + f, filenametmp)

        print('root',root) #当前目录路径  
        # print('dirs',dirs) #当前路径下所有子目录  
        print('files',files) #当前路径下所有非目录子文件 


# publish server 
# docker build -t jsmer/server:1.0 . 
# docker run -p 11001:11001 --name jsmer-server --restart=always -d jsmer/server:1.0
#
pubfilepath = '.publish'
version = ''
pubfilepath = pubfilepath + '/' + version
pubfile = pubfilepath + '/flask_web/'

if os.path.exists(pubfile):
    shutil.rmtree(pubfile)

mkdir(pubfile)
copys('appdata',pubfile)
copys('area',pubfile)
copys('entity',pubfile)
copys('webCore',pubfile)
copyfile('config-pro.py',pubfile + 'config.py')
copyfile('app.py',  pubfile + 'app.py')
copyfile('Dockerfile',  pubfile)
copyfile('gunicorn_conf.py',  pubfile)
copyfile('requirements.txt',  pubfile)

# with open(pubfile + 'winbuild.bat', 'w') as f1:
#     f1.write('virtualenv venv\n')
#     f1.write('venv\Scripts\python -m pip install --upgrade pip\n')
#     f1.write('venv\Scripts\pip3 install -r ./requirements.txt\n')

