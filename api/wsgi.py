# -*- coding: utf-8 -*-
"""`app.api.wsgi` package.

Contains the Application API/AJAX services.
"""

__all__ = ('api', )


import bottle
from bottle.ext.neck import StripPathMiddleware
from bottle.ext.smart_filters import SmartFiltersPlugin
from api.handlers import search_api, news_api


api = StripPathMiddleware(bottle.Bottle())
api.install(SmartFiltersPlugin())

api.get('/search')(search_api)
api.get('/news')(news_api)
