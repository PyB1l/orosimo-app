# -*- coding: utf-8 -*-
"""`orosimo-app` settings module.

Provides basic configuration variables for app.
"""

from pgtools import DBPoolEngine
from snaql.factory import Snaql
from os import path


POSTGRES = {
    'pool_size': 10,
    'pool_type': 'threaded',
    'debug': True,
    'host': '212.47.240.141',
    'port': 5432,
    'user': 'pav',
    'password': 'iverson',
    'database': 'oroshmoDB'
}


SERVER_OPTS = {
    'host': '0.0.0.0',
    'port': 8081,
    'server': 'cherrypy',
    'reloader': True
}


def query_builder(folder='', query_file=None, namespace=None):
    """Basic Query builder class factory from .sql templates

    Args:
        folder (str): Query folder path.
        query_file (str): Query file name.
        namespace (str): Query name_space

    Returns:
        A Snaql instance.
    """

    loader = Snaql(path.abspath(path.dirname(namespace)), folder)

    return loader.load_queries(query_file)


class DBEngine(object):
    """Data base Engine singleton factory.
    """

    engine_instance = None

    @classmethod
    def make(cls, **kwargs):
        if not cls.engine_instance:
            print('Initialization')
            cls.engine_instance = DBPoolEngine(**kwargs)
        return cls.engine_instance
