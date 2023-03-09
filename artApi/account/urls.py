from rest_framework.routers import SimpleRouter

from .views import FavoriteViewSet, RequestViewSet

__all__ = ['urlpatterns']

app_name = 'account_api'

accountRouter = SimpleRouter()

accountRouter.register(r'favorites', viewset=FavoriteViewSet, basename='favorite')
accountRouter.register(r'requests', viewset=RequestViewSet, basename='request')

urlpatterns = accountRouter.urls
