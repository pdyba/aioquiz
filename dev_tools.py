#!/usr/bin/env python3.5
# encoding: utf-8
from inspect import getmembers

import views
from views.utils import HTTPModelClassView
from utils import color_print

def get_all_views():
    v = []
    for member in getmembers(views):
        try:
            name, view = member
            if not issubclass(view, HTTPModelClassView) or view == HTTPModelClassView:
                if 'View' in name:
                    print(name, 'skipping')
                continue
        except:
            continue
        try:
            v.append((name, (view._urls)))
        except AttributeError:
            print(view, 'no URLS provided')
    return v


def get_all_views_and_routs(afilter=None):
    v = get_all_views()
    for view in sorted(v, key=lambda a: a[0]):
        if afilter:
            if afilter in view[0].lower():
                print(view[0])
                print('\t', view[1])
        else:
            print(view[0])
            print('\t', view[1])
    color_print('Views: ', len(v), color='blue')


def get_all_routs():
    view = get_all_views()
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

get_all_views_and_routs()
get_all_routs()
