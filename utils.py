# !/usr/bin/python3.5
from functools import wraps
import hashlib
import logging


async def format_dict_to_columns(adict):
    return [[a, adict[a]] for a in adict]


def get_args(args_dict):
    for arg, val in args_dict.items():
        if isinstance(val, list):
            args_dict[arg] = {
                'true': True,
                'True': True,
                'false': False,
                'False': False
            }.get(val[0], val[0])
    return args_dict


def safe_del_key(data, unwanted_key):
    """
    safe deleter of keys
    :param data: dict
    :param unwanted_key: str or list
    :return:
    """
    if isinstance(unwanted_key, str):
        if unwanted_key in data.keys():
            del data[unwanted_key]
    elif isinstance(unwanted_key, list):
        for ukey in unwanted_key:
            data = safe_del_key(data, ukey)
    return data


class SingletonDecorator:
    def __init__(self, a_class):
        self.a_class = a_class
        self.instance = None

    def __call__(self, args, *kwargs):
        if not self.instance:
            self.instance = self.a_class(*args, **kwargs)
            self.instance.__wrapped__ = self
        return self.instance


def error_catcher(function, default_return=False):
    @wraps(function)
    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as error:
            # Check if logger is in 'self'
            # If function is class method, use default logger from class
            # Otherwise use default logger from this module
            if args and hasattr(args[0], 'logger'):
                args[0].logger.exception(error)
            else:
                logging.exception(error)
            return default_return
    return wrapped


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
