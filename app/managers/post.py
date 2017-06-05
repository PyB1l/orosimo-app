from lunatic import QueryManager, QueryManagerError
from settings import POSTGRES_v2
from app.engines.postgres import PostgresEngine
from app.managers.base import BaseStorageManager


class PostManager(BaseStorageManager):
    """Post Model storage manager.
    """

    __slots__ = ('model', )

    engine = QueryManager(engine=PostgresEngine.make(**POSTGRES_v2))
    query_dir = 'backend'
    query_file = 'post.sql'
    query_parent = __file__

    def list(self, limit, offset, fields):
        """List post objects.
        """
        records = self._engine.list(
            limit=limit or None,
            offset=offset or 0,
            fetch_many=True
        )

        return [self.model(**post).serialize(*fields or []) for post in records]

    def create(self, model_instance, fields):
        """Create a new Post object.
        """
        post = self._engine.create(
            title=model_instance.title,
            body=model_instance.body,
            img=model_instance.img,
            fetch_many=False
        )

        self.model(**post).serialize(*fields or []) if post else None

    def retrieve(self, uid, fields):
        """Retrieve a single Post object based on UID.
        """
        post = self._engine.retrieve(uid=uid, fetch_many=False)

        return self.model(**post).serialize(*fields or []) if post else None

    def delete(self, uid, fields):
        """Delete a single Post object based on UID.
        """
        post = self._engine.delete(uid=uid, fetch_many=False)

        return self.model(**post).serialize(*fields or []) if post else None

    def count(self):
        """Count Post objects in storage.
        """

        total = self._engine.count(fetch_many=False)

        return total.get('total')
