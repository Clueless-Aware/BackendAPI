from rest_framework.routers import SimpleRouter

from .views import ArtworkViewSet

__all__ = ['urlpatterns']

app_name = 'artworks_api'

artworkRouter = SimpleRouter()

artworkRouter.register(r'artworks', viewset=ArtworkViewSet, basename='artwork')

urlpatterns = artworkRouter.urls
