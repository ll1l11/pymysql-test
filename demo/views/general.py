# -*- coding: utf-8 -*-
from flask import Blueprint
from flask.views import MethodView


bp = Blueprint('general', __name__)


class IndexView(MethodView):

    def get(self):
        return 'index'


bp.add_url_rule('/', view_func=IndexView.as_view('index'))
