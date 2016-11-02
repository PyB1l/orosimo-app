import bottle
from bottle_neck import StripPathMiddleware, Router
from admin.handlers import login, logout, index, post
from admin.api import PostsAPIHandler, SuccessAPIHandler

wsgi = StripPathMiddleware(bottle.Bottle())

router = Router()

router.register_handler(PostsAPIHandler, '/api/post')
router.register_handler(SuccessAPIHandler, '/api/success')

wsgi.get('/')(index)
wsgi.get('/post')(post)
wsgi.get('/logout')(logout)
wsgi.post('/login')(login)
wsgi.get('/login')(login)


router.mount(wsgi)
