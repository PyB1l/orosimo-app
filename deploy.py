import app
import bottle
import settings

app_container = bottle.Bottle()

app_container.mount('/beta-version', app.wsgi)

if __name__ == '__main__':

    bottle.debug(True)

    bottle.run(
        app=app_container,
        **settings.SERVER_OPTS
    )
