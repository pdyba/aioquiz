# !/usr/bin/python3.5

import logging
import sys


def get_logger(name):
    """
    Setting options for logger
    :param name: str
    """
    a_logger = logging.getLogger(name)
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname).5s - %(name)5.5s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)
    a_logger.addHandler(console_handler)
    a_logger.setLevel(logging.INFO)
    a_logger.propagate = False
    return a_logger

logger = get_logger('aioquiz')
