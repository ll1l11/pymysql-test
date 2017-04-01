# -*- coding: utf-8 -*-
from ..core import db
from ..helpers import JSONSerializer


class BaseModel(db.Model, JSONSerializer):
    __abstract__ = True
