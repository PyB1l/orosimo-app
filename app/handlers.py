# -*- coding: utf-8 -*-
"""`app` package.

Contains the Application web handlers.
"""


import bottle
import math
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


@bottle.jinja2_view('app/post_single.html')
def post_retrieve(uid):
    """Retrieve a blog post.
    """
    post = PostModel.get(uid=uid)
    if not post:
        bottle.abort(404)
    return {'page_breadcrumb': u'NEA', 'post': post}


@bottle.jinja2_view('app/post_list.html')
def post_list():
    """Default pagination is 3.
    """
    page = bottle.request.query.get('page', type=int) or 1

    posts = PostModel.all(limit=3, offset=3*(page - 1))

    total_pages = int(math.ceil(PostModel.count() / 3))

    pagination = [{'page': '/posts?page={}'.format(index), "index": index} for index in range(1, total_pages-1)]

    current_page = page

    return {'page_breadcrumb': u'ΝEA', 'posts': posts, 'pagination': pagination, 'page': current_page}


@bottle.jinja2_view('404.html')
def not_found(error):
    return {"error": "Not Found"} if error else {}


@bottle.jinja2_view('google5c7b68b49a8b8161.html')
def google_bot():
    return {}
