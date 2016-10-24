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

    fields = ('id', 'title', 'body', 'img', 'posted_at')

    @classmethod
    def get_latest(cls, limit, *fields):
        """
        """
        try:
            qs = cls.query.get_latest(limit=limit)
            records = cls.engine.query(qs, fetch_opts='many')

        except (DBAPIError, SnaqlException) as error:
            raise Exception(error.args[0])

        return [cls.serialize(record, *fields) for record in records]

    @classmethod
    def get(cls, uid, *fields):
        try:
            qs = cls.query.get(uid=uid)
            record = cls.engine.query(qs, fetch_opts='single')

        except (DBAPIError, SnaqlException) as error:
            raise Exception(error.args[0])

        return cls.serialize(record, *fields) if record else None

    @classmethod
    def all(cls, limit=None, offset=None, *fields):
        try:
            qs = cls.query.all(limit=limit, offset=offset)
            records = cls.engine.query(qs, fetch_opts='many')
        except (DBAPIError, SnaqlException) as error:
            raise Exception(error.args[0])

        return [cls.serialize(record, *fields) for record in records]

    @classmethod
    def serialize(cls, model, *fields):
        """Serialize to json a
        Args:
            model:

        Returns:
            A dict with serialized data.
        """

        if fieds:
            return {field: model.get(field) for field in fields}

        return {field: model.get(field) for field in cls.fields}
