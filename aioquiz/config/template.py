#!/usr/bin/env python3.5
# encoding: utf-8
DEFAULT_USER = 1


class SERVER:
    NAME = ''
    SCHEME = 'https'
    IP = '127.0.0.1'
    PORT_HTTP = 10080
    PORT_HTTPS = 10443
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
