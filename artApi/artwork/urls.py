from rest_framework.routers import SimpleRouter

from .views import ArtworkViewSet

__all__ = ['urlpatterns']

artworkRouter = SimpleRouter()

artworkRouter.register(r'artworks', viewset=ArtworkViewSet, basename='artwork')

urlpatterns = artworkRouter.urls
