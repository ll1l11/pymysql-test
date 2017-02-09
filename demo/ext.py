# -*- coding: utf-8 -*-
from werkzeug.local import LocalProxy
from flask import current_app
from flask_sqlalchemy import SQLAlchemy


logger = LocalProxy(lambda: current_app.logger)
db = SQLAlchemy()
