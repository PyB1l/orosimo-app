from bottle_neck import Router
from app.api.views import SuccessAPIViewSet, PostAPIViewSet


api_router = Router()

api_router.register_handler(SuccessAPIViewSet, '/success')
api_router.register_handler(PostAPIViewSet, '/posts')
