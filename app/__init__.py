# -*- coding: utf-8 -*-
"""`app` package.

Contains the Application wsgi callable.
"""

__all__ = ('wsgi', )

import functools

import bottle
from bottle.ext.neck import StripPathMiddleware

#  import mount
from api import api
from admin import wsgi as admin_wsgi

from app.handlers import index_handler, list_handler, register_handler

wsgi = StripPathMiddleware(bottle.Bottle())

wsgi.mount('/admin', admin_wsgi)
wsgi.mount('/api', api)

wsgi.get('/')(index_handler)
wsgi.get('/studies')(list_handler)
wsgi.get('/register')(register_handler)
wsgi.route("/static/<filename:path>")(functools.partial(bottle.static_file, root='static/'))
