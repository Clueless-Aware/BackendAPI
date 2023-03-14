from rest_framework.routers import SimpleRouter

from .views import UserViewSet, BookmarkViewSet

__all__ = ['urlpatterns']

app_name = 'artworks_api'

userRouter = SimpleRouter()

userRouter.register(r'users', viewset=UserViewSet, basename='user')
userRouter.register(r'bookmarks', viewset=BookmarkViewSet, basename='bookmark')

urlpatterns = userRouter.urls
