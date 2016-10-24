import bottle
from bottle.ext.neck import StripPathMiddleware
from admin.handlers import login, logout, index, post

wsgi = StripPathMiddleware(bottle.Bottle())

wsgi.get('/')(index)
wsgi.get('/post')(post)
wsgi.get('/logout')(logout)
wsgi.post('/login')(login)
wsgi.get('/login')(login)
