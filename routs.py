#!/usr/bin/env python3.5
# encoding: utf-8
from inspect import getmembers
from os.path import abspath
from os.path import dirname
from os.path import join

import views
from views.utils import HTTPModelClassView
from utils import color_print

dir_name = dirname(abspath(__file__))


def add_static(app):
    app.static('/', join(dir_name, 'static/index.html'))
    app.static('/css/', join(dir_name, 'static/css'))
    app.static('/fonts', join(dir_name, 'static/fonts/'))
    app.static('/js', join(dir_name, 'static/js/'))
    app.static('/images', join(dir_name, 'static/images'))
    app.static('/lessons', join(dir_name, 'static/lessons'))
    app.static('/partials', join(dir_name, 'static/partials'))
    app.static('/favicon.ico', join(dir_name, 'static/images/favicon.ico'))
    return app


def add_urls(app):
    count_cls = 0
    count_urls = 0

    for member in getmembers(views):
        try:
            name, view = member
            if not issubclass(view, HTTPModelClassView) or view == HTTPModelClassView:
                if 'View' in name:
                    color_print(name, 'skipping', color='yellow')
                continue
        except:
            continue
        try:
            if isinstance(view._urls, list):
                count_cls += 1
                for url in view._urls:
                    app.add_route(view.as_view(), url)
                    count_urls += 1
            elif isinstance(view._urls, str):
                app.add_route(view.as_view(), view._urls)
                count_cls += 1
                count_urls += 1
            else:
                color_print("Something is missing: ", view._get_name(), view._urls, color='yellow')
        except AttributeError:
            color_print(view, 'no URLS provided', color='red')

    color_print('Using {} classes with {} urls'.format(count_cls, count_urls), color='blue')
    return app