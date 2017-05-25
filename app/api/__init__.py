from app.api.urls import api_router
from bottle import Bottle
from bottle_neck import StripPathMiddleware, WSResponse
import ujson


api = StripPathMiddleware(Bottle())

api_router.mount(api)

error_handler = lambda error: ujson.dumps(WSResponse.from_status(
    status_line=error.status_line, msg=error.body
))


api.error(400)(error_handler)
api.error(401)(error_handler)
api.error(403)(error_handler)
api.error(404)(error_handler)
api.error(405)(error_handler)
api.error(502)(error_handler)
api.error(503)(error_handler)