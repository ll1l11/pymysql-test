# -*- coding: utf-8 -*-


class Config(object):
    DEBUG = True
    SECRET_KEY = '\xd4m1<w\x15\xe2?\x1e\xe3'

    # Flask-SQLAlchemy config
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/kfdda'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_RECYCLE = 10

    # Celery config
    CELERY_BROKER_URL = 'redis://127.0.0.1:6379/1'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'

    # Flask-Mail config
    MAIL_SERVER = 'smtp.exmail.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'you@exampl.ecom'
    MAIL_PASSWORD = 'your email password'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
