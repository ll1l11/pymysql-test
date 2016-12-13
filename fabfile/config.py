# -*- coding: utf-8 -*-
import os.path
import re
import ConfigParser

DOMAIN = 'www.example.com'
REPOSITORY = 'https://github.com/codeif/flask-demo.git'
# REPOSITORY = 'git@github.com:codeif/flask-demo.git'
DEFAULT_BRANCH = ''


# read from uwsgi.ini
config = ConfigParser.ConfigParser()
uwsgi_ini_file = os.path.join(os.path.dirname(__file__), '../uwsgi.ini')
config.read(uwsgi_ini_file)
items = dict(config.items('uwsgi'))

pythonpath = items['pythonpath']
m = re.search('/(\w+)/www', pythonpath)
if m:
    NAME = m.group(1)
else:
    NAME = 'demo'
WEB_ROOT_DIR = os.path.dirname(pythonpath)
# WEB_ROOT_DIR = '/srv/' + NAME
TOUCH_FILE = items.get('touch-reload')
VIRTUALENV_NAME = items['virtualenv'].rsplit('/', 1)[-1]
SOCKET = items['socket']

logto = items.get('logto')
if logto:
    UWSGI_LOG_DIR = os.path.dirname(logto)
else:
    UWSGI_LOG_DIR = None
