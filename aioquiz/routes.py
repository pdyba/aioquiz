#!/usr/bin/env python3.5
# encoding: utf-8
from inspect import getmembers
from os.path import abspath
from os.path import dirname
from os.path import join

import views
from views.utils import MCV
from utils import color_print

dir_name = dirname(abspath(__file__))


def add_static(app):
    app.static('/', join(dir_name, '../frontend/index.html'))
    app.static('/dist', join(dir_name, '../frontend/dist/'))
    app.static('/images', join(dir_name, '../static/images'))
    app.static('/lesson_source', join(dir_name, '../lesson_source/'))
    app.static('/favicon.ico', join(dir_name, '../static/images/favicon.ico'))
    return app


def get_all_views(add_views=True, names=False, urls=False):
    view_list = []
    for member in getmembers(views):
        try:
            name, view = member
            if not issubclass(view, MCV) or view == MCV:
                if 'View' in name:
                    color_print(name, 'skipping', color='yellow')
                continue
            if name.endswith('MCV'):
                color_print(name, 'skipping', color='white')
                continue
        except:
            continue
        try:
            assert view._urls
            temp = []
            if names:
                temp.append(name)
            if add_views:
                temp.append(view)
            if urls:
                temp.append(view._urls)
            assert len(temp) != 0
            if len(temp) == 1:
                temp = temp[0]
            else:
                temp = tuple(temp)
            view_list.append(temp)
        except (AttributeError, AssertionError):
            if 'Base' in name and 'Common' in name:
                color_print(name, 'skipping', color='white')
            else:
                color_print(view, 'no URLS provided', color='red')
    return view_list


def add_urls(app):
    count_cls = 0
    count_urls = 0

    for view in get_all_views():
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

    color_print('Using {} classes with {} urls'.format(count_cls, count_urls), color='blue')
    return app
