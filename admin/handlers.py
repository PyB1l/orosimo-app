from bottle import jinja2_view, jinja2_template, request, redirect, response
from functools import wraps
import time

server_secret = '@^$^&#^QWERTY'


def authenticate(username, password):
    return username == 'oroshmo_admin' and password == 'iverson@87'


def logout():
    response.set_cookie(
        '__utmb',
        '',
        secret=server_secret,
        expires=time.time() - (3600 * 24 * 365),
        domain='pav-pc',
        path='/'
    )

    return redirect('/admin')


def login():
    """Base login functionality.
    """
    if request.method == 'POST':

        print('POST detected')

        username = request.forms.get('username') or ''
        password = request.forms.get('password') or ''

        if not authenticate(username, password):
            return jinja2_template('admin/login.html', {"errors": u"Λάθος χρήστης /η κωδικός"})

        response.set_cookie(
            '__utmb',
            'oro_admin',
            secret=server_secret,
            expires=time.time() + (3600 * 24 * 365),
            domain='pav-pc',
            path='/'
        )

        redirect('/admin')

    return jinja2_template('admin/login.html')


def login_required(callback):
    """Login required decorator for bottle views.
    """
    @wraps(callback)
    def _wrapped(*args, **kwargs):
        if request.get_cookie('__utmb', secret=server_secret):
            return callback(*args, **kwargs)
        redirect('/admin/login')

    return _wrapped


@login_required
@jinja2_view('admin/blank.html')
def index():
    return {}
