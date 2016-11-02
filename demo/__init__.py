# -*- coding: utf-8 -*-
from . import factory
from .helpers import register_blueprints


def create_app(config=None):
    app = factory.create_app(config)

    module_prefix = __name__ + '.views.'
    package_path = app.root_path + '/views'
    register_blueprints(app, module_prefix, package_path)

    return app
