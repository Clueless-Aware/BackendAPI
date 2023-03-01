from rest_framework.routers import SimpleRouter

from .views import AccountViewSet, FavoriteViewSet

__all__ = ['urlpatterns']

app_name = 'account_api'

userRouter = SimpleRouter()

userRouter.register(r'accounts', viewset=AccountViewSet, basename='account')
userRouter.register(r'favorites', viewset=FavoriteViewSet, basename='favorites')

urlpatterns = userRouter.urls
