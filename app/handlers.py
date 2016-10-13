# -*- coding: utf-8 -*-
"""`app` package.

Contains the Application web handlers.
"""


import bottle


@bottle.jinja2_view('index.html')
def index_handler():
    return {}


@bottle.jinja2_view('pages/studies.html')
def list_handler():
    return {}
