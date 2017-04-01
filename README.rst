Flask-Demo
==========

测试服运行::

    python manage.py [-c kfdda.config.YourConfig] runsert -p 8080

正式服可以使用uwsgi

fabric的配置参考 `dansimau/flask-bootstrap <https://github.com/dansimau/flask-bootstrap>`_

- `A Better Pip Workflow <http://www.kennethreitz.org/essays/a-better-pip-workflow>`_

- password的保存

- @hybrid_property的使用

- overholt_

只保留最新的N个tag::

    ./tags.sh

secret_key生成方式::

    In [1]: import os
    In [2]: os.urandom(10)
    Out[2]: '\xd4m1<w\x15\xe2?\x1e\xe3'


Celery的supervisor配置::

    [program:kfdda-celery]
    environment=KFDDA_APP_SETTINGS="kfdda.config.ProductionConfig"
    command=/home/ubuntu/.virtualenvs/kfdda/bin/celery -A kfdda.tasks worker --loglevel=INFO

    directory=/srv/kfdda/www
    user=www-data
    numprocs=1
    stdout_logfile=/var/log/celery/kfdda-stdout.log
    stderr_logfile=/var/log/celery/kfdda-stderr.log
    autostart=true
    autorestart=true
    startsecs=10

    ; Need to wait for currently executing tasks to finish at shutdown.
    ; Increase this if you have very long running tasks.
    stopwaitsecs = 600

    ; When resorting to send SIGKILL to the program to terminate it
    ; send SIGKILL to its whole process group instead,
    ; taking care of its children as well.
    killasgroup=true

    ; Set Celery priority higher than default (999)
    ; so, if rabbitmq is supervised, it will start first.
    priority=1000


.. _overholt: https://github.com/mattupstate/overholt

