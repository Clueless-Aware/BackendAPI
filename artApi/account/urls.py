from rest_framework.routers import SimpleRouter

from .views import FavoriteViewSet

__all__ = ['urlpatterns']

app_name = 'account_api'

userRouter = SimpleRouter()

userRouter.register(r'favorites', viewset=FavoriteViewSet, basename='favorites')

urlpatterns = userRouter.urls
