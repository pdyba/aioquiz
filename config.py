try:
    from config_dev import *
    print('using dev config')
except:
    try:
        from config_prod import *
        print('using prod config')
    except:
        class EMAIL:
            SERVER = ''
            PORT = 465
            USERNAME = ''
            PASSWORD = ''

    class DB:
        HOST = '127.0.0.1'
        DB = 'postgres'
        USER = 'aiopg'
        PASSWORD = 'aiopg'


    class REGEMAIL:
        TEXT_PL = """
        Cześć {name}!
        Dziękujemy za rejestrację na warsztat weekendowy PyLadies.start() w Poznaniu w dniach 23-24 września.
        Proszę potwierdź swój adres mailowy klikając w poniższy link:

        http://{server}/api/activation/{uid}/{acode}

        Zapraszamy do śledzenia wydarzenia na FB:


        Dziękujemy!
        Pozdrowienia!
        PyLadies Poznań Team

        """
        TEXT_EN = """
        Hi {name},
        Thanks for registering for PyLadies.Start() workshop in Poznan on 23-24.09.2017.
        Please confirm your e-mail clicking this link:
        http://{server}/api/activation/{uid}/{acode}

        Follow facebook event for the latest infatuation:


        Thanks and good luck !
        Cheers
        PyLadies Poznan Team
        """
        SUBJECT_PL = 'PyLadies.start() Potwierdzenie rejestarcji'
        SUBJECT_EN = 'PyLadies.start() Workshops Registration Confirmation'
