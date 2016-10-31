import app
import bottle
import settings


if __name__ == '__main__':

    bottle.debug(True)

    bottle.run(
        app=app.wsgi,
        **settings.SERVER_OPTS
    )
