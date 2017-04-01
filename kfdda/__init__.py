# -*- coding: utf-8 -*-
from flask import jsonify
from . import factory
from .helpers import register_blueprints
from .exceptions import CustomException, FormValidationError


def create_app(config=None):
    app = factory.create_app(config)

    configure_error_handles(app)

    # register blueprints
    register_blueprints(app, __name__ + '.views')

    return app


def configure_error_handles(app):
    @app.errorhandler(CustomException)
    def teddy_exception_handler(e):
        return jsonify(errcode=e.errcode, errmsg=e.errmsg)

    @app.errorhandler(FormValidationError)
    def form_validation_error_handler(e):
        return jsonify(errcode=e.errcode, errmsg=e.errmsg, errors=e.errors)
