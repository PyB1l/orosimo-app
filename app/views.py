# -*- coding: utf-8 -*-
"""`app` package.

Contains the Application web handlers.
"""


import bottle
import math
from app.models import Post, Success
from app.services.email import mail_service
from bottle_neck import BaseHandler, WSResponse


class HomeView(BaseHandler):
    """Home page View
    """
    def get(self):
        """Home page GET handler.
        """
        posts = Post.manager.list(limit=3, offset=0, fields=[])
        context = {'posts': posts}
        return self.render('index.html', context)


class StudiesView(BaseHandler):
    def get(self):
        context = {'page_breadcrumb': u'ΟΔΗΓΟΣ ΣΠΟΥΔΩΝ'}
        return self.render('app/studies.html', context)


class RegisterView(BaseHandler):

    response_factory = WSResponse

    def get(self):
        context = {'page_breadcrumb': u'ΕΓΓΡΑΦΗ'}
        return self.render('app/register.html', context)

    def post(self):
        mail_context = self.request.json

        if mail_service('info@oroshmo.gr', mail_context):
            return self.response_factory.ok(data={'completed': True})

        return self.response_factory.ok(data={'completed': False})


class SuccessView(BaseHandler):
    def get(self):
        context = {'page_breadcrumb': u'ΕΠΙΤΥΧΙΕΣ'}
        return self.render('app/success.html', context)


class GoogleView(BaseHandler):
    def get(self):
        return self.render('google5c7b68b49a8b8161.html', {})


class PostView(BaseHandler):
    def get(self, uid=None):
        """List all Post models or retrieve a single record based on UID.
        """

        if uid:
            post = Post.manager.retrieve(uid=uid, fields=[])
            if not post:
                bottle.abort(404)
            context = {'page_breadcrumb': u'NEA', 'post': post}
            template = 'app/post_single.html'

        else:
            page = self.request.query.get('page', type=int) or 1

            posts = Post.manager.list(limit=3, offset=3 * (page - 1), fields=[])

            total_pages = int(math.ceil(Post.manager.count() / 3))

            pagination = [{'page': '/posts?page={}'.format(index), "index": index} for index in
                          range(1, total_pages - 1)]

            current_page = page

            context = {'page_breadcrumb': u'ΝEA', 'posts': posts, 'pagination': pagination, 'page': current_page}

            template = 'app/post_list.html'

        return self.render(template, context)

