# -*- coding: utf-8 -*-

from .core import logger
from .factory import create_celery_app

celery = create_celery_app()


@celery.task
def add(x, y):
    logger.debug('task execute add')
    return x + y
