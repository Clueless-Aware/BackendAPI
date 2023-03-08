from rest_framework.routers import SimpleRouter

from .views import ArtworkViewSet, ArtistViewSet

__all__ = ['urlpatterns']

app_name = 'artworks_api'

artworkRouter = SimpleRouter()

artworkRouter.register('artworks', viewset=ArtworkViewSet, basename='artwork')
artworkRouter.register('artists', viewset=ArtistViewSet, basename='artist')

urlpatterns = artworkRouter.urls
