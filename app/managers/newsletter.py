from lunatic import QueryManager, QueryManagerError
from settings import POSTGRES_v2
from app.engines.postgres import PostgresEngine
from app.managers.base import BaseStorageManager


class NewsLetterManager(BaseStorageManager):
    """Newsletter Model storage manager.
    """

    __slots__ = ('model', )

    engine = QueryManager(engine=PostgresEngine.make(**POSTGRES_v2))
    query_dir = 'backend'
    query_file = 'newsletter.sql'
    query_parent = __file__

    def list(self, fields):
        """List post objects.
        """
        records = self._engine.list(
            fetch_many=True
        )

        return [self.model(**post).serialize(*fields or []) for post in records]

    def create(self, email, fields):
        """Retrieve a single Post object based on UID.
        """
        newsletter = self._engine.create(email=email, fetch_many=False)

        return self.model(**newsletter).serialize(*fields or []) if newsletter else None

