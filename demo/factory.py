# -*- coding: utf-8 -*-
import os
from celery import Celery
from flask import Flask


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = os.environ.get('FLASK_DEMO_SETTINGS', 'demo.config.Config')
    app.config.from_object(config)

    return app


def create_celery_app(app=None):
    app = app or create_app()
    celery = Celery()
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery
