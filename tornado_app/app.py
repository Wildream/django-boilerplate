import time
from importlib import import_module

import tornado.web
from django.conf import settings
from tornado import gen
from tornado.ioloop import IOLoop

from tornado_app.urls import urlpatterns

session_engine = import_module(settings.SESSION_ENGINE)


@gen.coroutine
def async_sleep(seconds):
    yield gen.Task(IOLoop.instance().add_timeout, time.time() + seconds)


def build_app():
    application = tornado.web.Application(urlpatterns, autoreload=True)
    return application


def run(port=None):
    if port is None:
        port = settings.TORNADO_APP_PORT
    app = build_app()
    app.listen(
        port,
        address=settings.TORNADO_APP_ADDRESS
    )
    IOLoop.instance().start()
