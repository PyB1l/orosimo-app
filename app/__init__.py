# -*- coding: utf-8 -*-
"""`app` package.

Contains the Application wsgi callable.
"""

__all__ = ('wsgi', )

import functools

import bottle
from bottle.ext.neck import StripPathMiddleware

#  import mount
from app.api import api
from app.urls import app_router
from admin import wsgi as admin_wsgi

wsgi = StripPathMiddleware(bottle.Bottle())

# Mount routing in app

app_router.mount(wsgi)

# Mount internal apps.

wsgi.mount('/admin', admin_wsgi)
wsgi.mount('/api/v1.0', api)

# Override error handlers.

wsgi.error(404)(lambda error: bottle.jinja2_template('404.html', {"error": "Not Found"}))
wsgi.error(405)(lambda error: bottle.jinja2_template('404.html', {"error": "Not Found"}))

# static files serving.

wsgi.route("/static/<filename:path>")(functools.partial(bottle.static_file, root='static/'))

