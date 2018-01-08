#!/usr/bin/env python3.5
# encoding: utf-8
from utils import color_print

from routes import get_all_views


def get_all_views_and_routes(afilter=None, with_routes=True):
    v = get_all_views(add_views=False, names=True, urls=True)
    for view in sorted(v, key=lambda a: a[0]):
        if afilter and afilter in view[0].lower():
            print(view[0])
            if with_routes:
                print('\t', view[1])
        else:
            print(view[0])
            if with_routes:
                print('\t', view[1])
    color_print('Views: ', len(v), color='blue')


def get_all_routes():
    view = get_all_views(add_views=False, names=True, urls=True)
    routes = []
    for v in view:
        if isinstance(v[1], list):
            for a in v[1]:
                routes.append(a)
        else:
            routes.append(v[1])
    for r in sorted(routes):
        if not r.startswith('/api'):
            color_print(r, color='red')
        else:
            print(r)
    color_print('routes: ', len(routes), color='blue')
    return routes

get_all_views_and_routes(with_routes=False)
get_all_routes()
