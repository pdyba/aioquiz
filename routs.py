#!/usr/bin/env python3.5
# encoding: utf-8
from inspect import getmembers
from os.path import abspath
from os.path import dirname
from os.path import join

import views
from views.utils import HTTPModelClassView

dir_name = dirname(abspath(__file__))


def add_static(app):
    app.static('/', join(dir_name, 'static/index.html'))
    app.static('/sum', join(dir_name, 'static/summary.html'))
    app.static('/js/vendor/', join(dir_name, 'static/js/vendor/'))
    app.static('/css/', join(dir_name, 'static/css'))
    app.static('/js', join(dir_name, 'static/js/'))
    app.static('/images', join(dir_name, 'static/images'))
    app.static('/partials', join(dir_name, 'static/partials'))
    app.static('/templates', join(dir_name, 'static/templates'))
    app.static('/lessons', join(dir_name, 'static/lessons'))
    app.static('/favicon.ico', join(dir_name, 'static/images/favicon.ico'))
    app.static('/dist', join(dir_name, 'static/dist'))
    return app


def add_urls(app):
    count_cls = 0
    count_urls = 0

    for member in getmembers(views):
        try:
            name, view = member
            if not issubclass(view, HTTPModelClassView) or view == HTTPModelClassView:
                if 'View' in name:
                    print(name, 'skipping')  # TODO: should be yellow
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
                print("Something is missing: ", view._get_name(), view._urls)
        except AttributeError:
            print(view, 'no URLS provided')  # TODO: should be in red

    print('Using {} classes with {} urls'.format(count_cls, count_urls))
    return app