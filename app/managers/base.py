# -*- coding: utf-8 -*-
"""`core.managers` module.

Provides `core` library storage manager utilities.
"""

from os import path


class BaseStorageManager(object):
    """Base Storage Manager class for Postgresql backends.

    Attributes:
        engine (object): A `lunatic.QueryManager` instance
        query_file (str): Query file name.
        query_dir (str): Query directory name.
    """

    engine = None
    query_file = ''
    query_dir = ''
    query_parent = ''

    __slots__ = ('model', )

    def __init__(self, model=None):  # pragma no cover
        """`BaseStorageManager` as `cached_classproperty`, `class_property`
        with model attribute.
        """
        self.model = model

    @property
    def _engine(self):  # pragma: no cover
        if self.engine.builder:
            return self.engine

        self.engine.load(
            query_parent=path.dirname(path.abspath(self.query_parent)),
            query_dir=self.query_dir,
            query_file=self.query_file
        )

        return self.engine
