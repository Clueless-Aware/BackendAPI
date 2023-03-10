from rest_framework.routers import SimpleRouter

from .views import UserViewSet

__all__ = ['urlpatterns']

app_name = 'artworks_api'

userRouter = SimpleRouter()

userRouter.register(r'users', viewset=UserViewSet, basename='user')

urlpatterns = userRouter.urls
