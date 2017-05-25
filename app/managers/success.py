from lunatic import QueryManager, QueryManagerError
from settings import POSTGRES_v2
from app.engines.postgres import PostgresEngine
from app.managers.base import BaseStorageManager


class SuccessManager(BaseStorageManager):
    """Success Model storage manager.
    """

    __slots__ = ('model', )

    engine = QueryManager(engine=PostgresEngine.make(**POSTGRES_v2))
    query_dir = 'backend'
    query_file = 'success.sql'
    query_parent = __file__

    def list(self, year, fields):
        """Retrieve a single Flight object based on UID.
        """
        records = self._engine.list(year=year, fetch_many=True)
        return [self.model(**success).serialize(*fields or []) for success in records]

    def years(self):
        """Retrieve a single Flight object based on UID.
        """
        records = self._engine.years(fetch_many=True)

        return records
