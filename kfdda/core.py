# -*- coding: utf-8 -*-
"""
    kfdda.core
    ~~~~~~~~~~~~

    flask-kfdda core module

    :copyright: (c) 2016 by codeif.
    :license: MIT, see LICENSE for more details.
"""

from werkzeug.local import LocalProxy
from flask import current_app
from flask_sqlalchemy import SQLAlchemy


logger = LocalProxy(lambda: current_app.logger)
db = SQLAlchemy()
