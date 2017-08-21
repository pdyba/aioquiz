try:
    from config_dev import *
except:
    print('no dev')
    try:
        from config_prod import *
    except:
        print('no_prod')
        class EMAIL:
            SERVER = ''
            PORT = 465
            USERNAME = ''
            PASSWORD = ''
