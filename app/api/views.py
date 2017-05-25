from bottle_neck import BaseHandler, route_method, WSResponse
from app.models import Success, Post
from schema_factory import SchemaError, SchemaFactoryError


class SuccessAPIViewSet(BaseHandler):
    """Success model API ViewSet.
    """

    base_endpoint = '/success'
    response_factory = WSResponse

    model = Success

    def get(self, year):
        """Retrieve success records per year
        """
        try:
            self.model(school_year=year)
        except (SchemaError, SchemaFactoryError) as error:
            self.abort(400, error.args[0])

        records = self.model.manager.list(year=year, fields=[])

        if not records:
            self.abort(404, 'Year {} down not exist'.format(year))

        return self.response_factory.ok(data=records)

    @route_method('GET', extra_part=True)
    def available(self):
        """Retrieve available years of success.
        """

        records = self.model.manager.years()
        for record in records:
            record['school_year'] = str(record['school_year'])

        return self.response_factory.ok(data={'years': records})


class PostAPIViewSet(BaseHandler):
    """Success model API ViewSet.
    """

    base_endpoint = '/posts'
    response_factory = WSResponse

    model = Post

    def get(self, uid=None):
        """Retrieve success records per year
        """

        if uid:
            try:
                self.model(id=uid)
            except (SchemaError, SchemaFactoryError) as error:
                self.abort(400, error.args[0])

            post = self.model.manager.retrieve(uid=uid, fields=[])

            if not post:
                return self.abort(404, 'No post found with UID `{}`.'.format(uid))

            return self.response_factory.ok(data=post)

        limit = int(self.request.query.get('limit')) or None

        post_list = self.model.manager.list(limit=limit, offset=None, fields=[])

        return self.response_factory.ok(data=post_list or [])
