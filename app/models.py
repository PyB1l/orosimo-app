# -*- coding: utf-8 -*-
"""`app.models` package.

Contains the external services for handling external functionality.
"""

from schema_factory import BaseSchema, StringNode, BooleanNode, IntegerNode
from pycom.attr import cached_classproperty
from app.managers.success import SuccessManager
from app.managers.post import PostManager


def uid_validator(value):
    return str(value).isnumeric()


class Success(BaseSchema):
    """Orosimo App success model.
    """
    id = StringNode(validators=[uid_validator])
    full_name = StringNode()
    school_year = IntegerNode()
    university = StringNode()
    promoted = BooleanNode(default=False)

    @cached_classproperty
    def manager(self):
        return SuccessManager(self)


class Post(BaseSchema):
    """Orosimo App Post model.
    """
    id = StringNode(validators=[uid_validator])
    title = StringNode()
    body = StringNode()
    img = StringNode()
    posted_at = StringNode()
    likes = IntegerNode()
    total_comments = IntegerNode()

    @cached_classproperty
    def manager(self):
        return PostManager(self)
