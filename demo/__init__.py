# -*- coding: utf-8 -*-
from . import factory
from .helpers import register_blueprints


def create_app(config=None):
    app = factory.create_app(config)

    # register blueprints
    register_blueprints(app, __name__ + '.views')

    return app
