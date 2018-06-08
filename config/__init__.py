#!/usr/bin/env python3.5
# encoding: utf-8
try:
    from config.config_dev import *
    print('using DEV config')
except ImportError:
    try:
        from config.config_prod import *
        print('using PROD config')
    except ImportError:
        from config.template import *
except Exception as err:
    print(err)
    print('error with config quitting')
    quit()

from config.emails_pl import ALL_EMAILS
from config.emails_pl import REGEMAIL
