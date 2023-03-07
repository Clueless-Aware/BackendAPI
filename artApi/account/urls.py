from rest_framework.routers import SimpleRouter

from .views import FavoriteViewSet, RequestViewSet

__all__ = ['urlpatterns']

app_name = 'account_api'

accountRouter = SimpleRouter()

accountRouter.register('favorites', viewset=FavoriteViewSet, basename='Favorites')
accountRouter.register('requests', viewset=RequestViewSet, basename='Requests')

urlpatterns = accountRouter.urls
