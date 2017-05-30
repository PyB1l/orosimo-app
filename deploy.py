import app
import bottle
import settings


if __name__ == '__main__':
    print(settings.DEBUG)
    bottle.debug(settings.DEBUG)

    bottle.run(
        app=app.wsgi,
        **settings.SERVER_OPTS
    )
