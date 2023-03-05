from rest_framework.routers import SimpleRouter

from .views import UserViewSet

__all__ = ['urlpatterns']

app_name = 'artworks_api'

artworkRouter = SimpleRouter()

artworkRouter.register(r'users', viewset=UserViewSet, basename='user')

urlpatterns = artworkRouter.urls
