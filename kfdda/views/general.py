# -*- coding: utf-8 -*-
from flask import Blueprint
from flask.views import MethodView

from ..core import db, logger
from ..exceptions import NoError, FormValidationError

from ..forms.login import LoginForm
from ..models.user import User
from ..tasks import add


bp = Blueprint('general', __name__)


class IndexView(MethodView):
    def get(self):
        users = User.query.all()
        return ''.join(x.phone for x in users)


class AddView(MethodView):
    def get(self):
        phone = '13800138000'
        email = 'me@codeif.com'
        password = '123456'
        user = User(phone=phone, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return 'ok'


class FormErrorView(MethodView):
    def get(self):
        form = LoginForm()
        if not form.validate():
            raise FormValidationError(form)
        raise NoError()


class CeleryTestView(MethodView):
    def get(self):
        add.delay(1, 3)
        return 'ok'


class ExceptionView(MethodView):
    def get(self):
        logger.error('this is error')
        assert 1 == 2
        return '1 == 2'

class LogView(MethodView):
    def get(self):
        logger.debug('log level debug')
        logger.info('log level info')
        logger.warn('log level warn')
        logger.error('log level error')
        return 'ok'

bp.add_url_rule('/', view_func=IndexView.as_view('index'))
bp.add_url_rule('/add', view_func=AddView.as_view('error'))
bp.add_url_rule('/form-error', view_func=FormErrorView.as_view('form_error'))
bp.add_url_rule('/celery-test',
                view_func=CeleryTestView.as_view('celery_test'))
bp.add_url_rule('/exception', view_func=ExceptionView.as_view('excepiton'))
bp.add_url_rule('/log', view_func=LogView.as_view('log'))
