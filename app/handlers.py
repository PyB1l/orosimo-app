# -*- coding: utf-8 -*-
"""`app` package.

Contains the Application web handlers.
"""


import bottle
from admin.models import PostModel, SuccessModel


@bottle.jinja2_view('index.html')
def index_handler():
    posts = PostModel.get_latest(limit=3)
    return {'posts': posts}


@bottle.jinja2_view('app/studies.html')
def list_handler():
    return {'page_breadcrumb': u'ΟΔΗΓΟΣ ΣΠΟΥΔΩΝ'}


@bottle.jinja2_view('app/register.html')
def register_handler():
    return {'page_breadcrumb': u'ΕΓΓΡΑΦΗ'}


@bottle.jinja2_view('app/success.html')
def success_handler():
    success_data = SuccessModel.all()
    return {'page_breadcrumb': u'ΕΠΙΤΥΧΙΕΣ', 'success_data': success_data}
