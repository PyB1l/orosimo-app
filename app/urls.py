from bottle_neck import Router
from app.views import HomeView, SuccessView, RegisterView, GoogleView, \
    StudiesView, PostView, AboutView


app_router = Router()


# Orosimo App Views.

app_router.register_handler(HomeView, '/')
app_router.register_handler(SuccessView, '/success')
app_router.register_handler(StudiesView, '/studies')
app_router.register_handler(AboutView, '/about')
app_router.register_handler(PostView, '/posts')
app_router.register_handler(RegisterView, '/register')

# Google SEO related Views
app_router.register_handler(GoogleView, '/google5c7b68b49a8b8161.html')
