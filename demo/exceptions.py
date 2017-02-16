# -*- coding: utf-8 -*-
import sys

current_module = sys.modules[__name__]


exceptions = [
    ('NoError', 0, 'OK'),
    ('LoginRequired', 1001, 'Login required.'),
    ('BindPhoneRequired', 1002, 'Bind phone required.'),
]


class CustomBaseException(Exception):
    errcode = 1000
    errmsg = 'Server Unkown Error.'

    def __init__(self, errmsg=None):
        if errmsg:
            self.errmsg = errmsg

    def __str__(self):
        return '%d: %s' % (self.errcode, self.errmsg)

    def __repr__(self):
        return '<%s \'%s\'>' % (self.__class__.__name__, self)


class CustomException(CustomBaseException):
    pass


for name, errcode, errmsg in exceptions:
    cls = type(name,
               (CustomException,),
               {'errcode': errcode, 'errmsg': errmsg})
    setattr(current_module, name, cls)


class FormValidationError(CustomBaseException):
    errcode = 2001
    errmsg = '表单验证错误'

    def __init__(self, form, errmsg=None):
        super(FormValidationError, self).__init__(errmsg)
        self.errors = form.errors
