# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField


class LoginForm(FlaskForm):
    email = StringField('Email')
