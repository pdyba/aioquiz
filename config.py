try:
    from config_prod import *
except:
    pass

try:
    from config_dev import *
except:
    class EMAIL:
        SERVER = ''
        PORT = 465
        USERNAME = ''
        PASSWORD = ''
