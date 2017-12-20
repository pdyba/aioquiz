#!/usr/bin/env python3.5
# encoding: utf-8
from inspect import getmembers

import views
from views.utils import HTTPModelClassView


def get_all_views_and_routs(afilter=None):
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
    for view in sorted(v, key=lambda a: a[0]):
        if afilter:
            if afilter in view[0].lower():
                print(view[0])
                print('\t', view[1])
        else:
            print(view[0])
            print('\t', view[1])

# get_all_views_and_routs(afilter='user')
get_all_views_and_routs()
