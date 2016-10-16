# -*- coding: utf-8 -*-
"""`app.models` package.

Contains the external services for handling external functionality.
"""

from pgtools import DBPoolEngine, DBAPIBackend, ViewField, DBAPIError
from pgtools.engine import EngineError


engine = DBPoolEngine(
    pool_size=20,
    pool_type="threaded",
    debug=True,
    host="212.47.240.141",
    port=5432,
    user="pav",
    password="iverson",
    database="oroshmoDB"
)


class ModelError(Exception):
    """Base Model Exception class.
    """
    pass


class AdminModel(DBAPIBackend):
    """Admin Database Schema Model
    """

    get_latest = ViewField()

    class Meta:
        schema = 'admin'


def admin_backend(action, fetch_opts='many', **params):
    """
    Args:
        action:
        fetch_opts:
        **params:

    Returns:

    """
    callback = getattr(AdminModel(), action) or None

    try:
        records = engine.query(callback(**params), fetch_opts=fetch_opts)

    except (EngineError, DBAPIError) as error:
        raise ModelError(error.args[0])

    return records
