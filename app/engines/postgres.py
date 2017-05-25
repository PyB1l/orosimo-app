from lunatic import DBEngine, DBRouter
import settings


class Singleton(object):
    """Simple singleton.
    """
    _instance = None
    _cls = None

    @classmethod
    def make(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls._cls(*args, **kwargs)
        return cls._instance


class PostgresEngine(Singleton):
    """Postgresql Engine singleton.
    """
    _cls = DBEngine
