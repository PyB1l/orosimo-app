# -*- coding: utf-8 -*-
"""Model redefinition based on snaql.
"""

from snaql.factory import Snaql, SnaqlException
from pgtools import DBAPIError
from settings import DBEngine, POSTGRES, query_builder
from os import path
import datetime


class SuccessModel(object):
    """Admin Success Model class.
    """
    query = query_builder(folder='db', query_file='success.sql', namespace=__file__)
    engine = DBEngine.make(**POSTGRES)

    @classmethod
    def available_years(cls):
        try:
            qs = cls.query.available_years()
            records = cls.engine.query(qs, fetch_opts='many')

        except (DBAPIError, SnaqlException) as error:
            raise Exception(error.args[0])

        return records

    @classmethod
    def all(cls):
        years = [record['school_year'] for record in cls.available_years()]

        total_success = dict()

        for year in years:
            total_success[year] = cls.get_year(year=year)

        return total_success

    @classmethod
    def get_year(cls, year):
        """Get year success models.
        """
        try:
            qs = cls.query.get_year(year=year)
            records = cls.engine.query(qs, fetch_opts='many')

        except (DBAPIError, SnaqlException) as error:
            raise Exception(error.args[0])

        return records

    @classmethod
    def get_promoted(cls):
        """Get year success models.
        """
        current_year = datetime.datetime.now().year

        try:
            qs = cls.query.get_promoted(year=current_year)
            records = cls.engine.query(qs, fetch_opts='many')

        except (DBAPIError, SnaqlException) as error:
            raise Exception(error.args[0])

        return records


class PostModel(object):
    """Admin Post model class.
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

        if fields:
            raw_model = {field: model.get(field) for field in fields}

        else:
            raw_model = {field: model.get(field) for field in cls.fields}

        if 'posted_at' in raw_model:
            raw_model['posted_at'] = str(raw_model['posted_at'])

        return raw_model
