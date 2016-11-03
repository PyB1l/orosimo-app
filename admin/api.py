# -*- coding: utf-8 -*-
"""`admin` application API module.
"""

from bottle_neck import WSResponse, BaseHandler, route_method
from admin.models import PostModel, SuccessModel
import bottle


class SuccessAPIHandler(BaseHandler):
    """Admin Success model API handler.
    """

    base_endpoint = '/success'

    model = SuccessModel

    @route_method('GET', extra_part=True)
    def available(self):
        """Retrieve available years of success.
        """

        records = self.model.available_years()
        for record in records:
            record['school_year'] = str(record['school_year'])

        return WSResponse.ok(data={'years': records})

    @route_method('GET', extra_part=True)
    def get_year(self, year):
        """Retrieve Success models by year
        """
        records = self.model.get_year(year)

        if not records:
            return WSResponse.not_found(errors=['Success for year {} don`t not exist'.format(year)])

        return WSResponse.ok(data=records)

    @route_method('GET', extra_part=True)
    def get_promoted(self):
        """Retrieve Success models by year
        """
        records = self.model.get_promoted()

        if not records:
            return WSResponse.not_found(errors=['Success for year {} don`t not exist'.format(year)])

        return WSResponse.ok(data=records)


class PostsAPIHandler(BaseHandler):
    """Admin Post model API handlers.
    """

    base_endpoint = '/post'

    model = PostModel

    def get(self, uid):
        """Retrieve a single Post model.
        """
        post = self.model.get(uid=uid)

        if not post:
            return WSResponse.not_found(errors=['Model with UID {} does not exist'.format(uid)])

        return WSResponse.ok(data=post)

    @route_method('POST', extra_part=True)
    def like(self, uid):
        """Add like to Post model.
        """

        model = self.model.add_like(uid)
        return WSResponse.ok(data=model)

    @route_method('POST', extra_part=True)
    def comment(self, uid):
        """Add like to Post model.
        """

        comment_data = self.request.json

        model = self.model.add_comment(uid=uid, **comment_data)
        return WSResponse.ok(data=model)

    @route_method('GET', extra_part=False)
    def list(self):
        """Retrieve all Posts.
        """
        limit = self.request.query.get('limit', type=int, default=100)
        offset = self.request.query.get('offset', type=int, default=0)
        posts = self.model.all(limit=limit, offset=offset)
        return WSResponse.ok(data=posts or [])

    @route_method('GET', extra_part=True)
    def get_latest(self, num):
        """Get N - latest post models..
        """

        latest_posts = self.model.get_latest(limit=num)

        return WSResponse.ok(data=latest_posts or [])
