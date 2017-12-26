#!/usr/bin/env python3.5
# encoding: utf-8
DEFAULT_USER = 1


class SERVER:
    IP = '0.0.0.0'
    PORT_HTTP = 80
    PORT_HTTPS = 443
    DEBUG = False
    WORKERS = 1
    # USE absolute path :)
    CERT = "./cert.pem"
    PRIVKEY = "./privkey.pem"


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
    """
    move to DB
    """
    TEXT_PL = """
    Cześć {name}!
    Dziękujemy za rejestrację na warsztaty PyLove.org w Poznaniu.
    Proszę potwierdź swój adres mailowy klikając w poniższy link:

    https://{server}/api/user/activation/{uid}/{acode}

    Pozdrowienia!
    PyLove.org Team

    """
    TEXT_EN = """
    Hi {name},
    Thanks for registering for PyLove.org workshops in Poznan.
    Please confirm your e-mail clicking this link:

    https://{server}/api/user/activation/{uid}/{acode}

    Cheers
    PyLove.org Team
    """
    SUBJECT_PL = 'PyLove.org Potwierdzenie rejestarcji'
    SUBJECT_EN = 'PyLove.org Registration Confirmation'


class MAINCONFIG:
    """
    move to DB
    """
    CIRITERIA = """
    how we should judge
    """