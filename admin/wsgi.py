import bottle
from bottle_neck import StripPathMiddleware, Router
from admin.handlers import login, logout, index, post, index_2, post_create
from admin.api import PostsAPIHandler, SuccessAPIHandler

wsgi = StripPathMiddleware(bottle.Bottle())

router = Router()

router.register_handler(PostsAPIHandler, '/api/post')
router.register_handler(SuccessAPIHandler, '/api/success')

wsgi.get('/2')(index_2)
wsgi.get('/')(index)
wsgi.get('/post/new')(post_create)
wsgi.get('/post')(post)
wsgi.get('/logout')(logout)
wsgi.post('/login')(login)
wsgi.get('/login')(login)


router.mount(wsgi)
