# -*- coding: utf-8 -*-
"""Model redefinition based on snaql.
"""

from snaql.factory import Snaql, SnaqlException
from pgtools import DBAPIError
from settings import DBEngine, POSTGRES, query_builder
from os import path


class PostModel(object):
    """Base post model class.
    """
    query = query_builder(folder='db', query_file='post.sql', namespace=__file__)
    engine = DBEngine.make(**POSTGRES)

    @classmethod
    def get_latest(cls, limit):
        """
        """
        try:
            qs = cls.query.get_latest(limit=limit)
            records = cls.engine.query(qs, fetch_opts='many')

        except (DBAPIError, SnaqlException) as error:
            raise Exception(error.args[0])

        return [cls.serialize(record) for record in records]

    @classmethod
    def get(cls, uid):
        try:
            qs = cls.query.get(uid=uid)
            record = cls.engine.query(qs, fetch_opts='single')

        except (DBAPIError, SnaqlException) as error:
            raise Exception(error.args[0])

        return cls.serialize(record) if record else None

    @classmethod
    def all(cls, limit=None, offset=None):
        try:
            qs = cls.query.all(limit=limit, offset=offset)
            records = cls.engine.query(qs, fetch_opts='many')
        except (DBAPIError, SnaqlException) as error:
            raise Exception(error.args[0])

        return [cls.serialize(record) for record in records]

    @staticmethod
    def serialize(model):
        """Serialize to json a
        Args:
            model:

        Returns:
            A dict with serialized data.
        """
        return {"id": model.get('id'), "title": model.get('title'), "body": model.get('body'),
                "img": model.get('img'), "posted": model.get('posted_at').strftime(format='%Y:%m:%d %H:%M:%S')}
