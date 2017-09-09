try:
    from config.config_dev import *
    print('using dev config')
except ImportError:
    try:
        from config.config_prod import *
        print('using prod config')
    except ImportError:
        from config.template import *
except Exception as err:
    print(err)
    print('error with config quitting')
    quit()

from config.emails_pl import ALL_EMAILS
