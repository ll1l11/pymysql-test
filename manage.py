# -*- coding: utf-8 -*-
"""
    manage
    ~~~~~~~~~~~~

    manage module

    :copyright: (c) 2016 by codeif.
    :license: MIT, see LICENSE for more details.
"""

from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from kfdda import create_app
from kfdda.core import db


manager = Manager(create_app)


@manager.command
def db_create_all():
    db.create_all()


manager.add_command('db', MigrateCommand)
manager.add_option('-c', '--config', dest='config', required=False)
manager.add_command('runserver', Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
)

if __name__ == '__main__':
    manager.run()
