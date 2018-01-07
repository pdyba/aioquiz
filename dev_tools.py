#!/usr/bin/env python3.5
# encoding: utf-8
from utils import color_print

from routes import get_all_views


def get_all_views_and_routs(afilter=None, with_routs=True):
    v = get_all_views(add_views=False, names=True, urls=True)
    for view in sorted(v, key=lambda a: a[0]):
        if afilter and afilter in view[0].lower():
            print(view[0])
            if with_routs:
                print('\t', view[1])
        else:
            print(view[0])
            if with_routs:
                print('\t', view[1])
    color_print('Views: ', len(v), color='blue')


def get_all_routs():
    view = get_all_views(add_views=False, names=True, urls=True)
    routs = []
    for v in view:
        if isinstance(v[1], list):
            for a in v[1]:
                routs.append(a)
        else:
            routs.append(v[1])
    for r in sorted(routs):
        if not r.startswith('/api'):
            color_print(r, color='red')
        else:
            print(r)
    color_print('Routs: ', len(routs), color='blue')
    return routs

get_all_views_and_routs(with_routs=False)
get_all_routs()
