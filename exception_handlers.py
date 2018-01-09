#!/usr/bin/env python3.5
# encoding: utf-8
import logging

from sanic.response import json

from sanic.exceptions import NotFound
from sanic.exceptions import RequestTimeout
from sanic.exceptions import ServerError


def handle_500s(request, exception):
    logging.error(' 500 ' + request.url)
    return json(
        {"msg": "Nope not gonna work"},
        status=500
    )


def handle_404s(request, exception):
    logging.error(' 404 ' + request.url)
    return json(
        {'msg': "Yep, I totally found the page: {}".format(request.url)},
        status=404
    )


def handle_timeout(request, exception):
    return json(
        {'msg': "I have been waiting too long sorry"},
        status=408
    )


def add_exception_handlers(app):
    app.error_handler.add(ServerError, handle_500s)
    app.error_handler.add(NotFound, handle_404s)
    app.error_handler.add(RequestTimeout, handle_timeout)
    return app
