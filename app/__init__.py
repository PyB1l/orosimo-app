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

from app.handlers import (index_handler, list_handler, register_handler, success_handler,
                          post_list, post_retrieve, not_found)

wsgi = StripPathMiddleware(bottle.Bottle())

wsgi.mount('/admin', admin_wsgi)
wsgi.mount('/api', api)

wsgi.error(404)(not_found)

wsgi.get('/')(index_handler)
wsgi.get('/studies')(list_handler)
wsgi.get('/register')(register_handler)
wsgi.get('/success')(success_handler)
wsgi.get('/posts')(post_list)
wsgi.get('/posts/<uid>')(post_retrieve)
wsgi.route("/static/<filename:path>")(functools.partial(bottle.static_file, root='static/'))
