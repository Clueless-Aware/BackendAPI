from rest_framework.routers import SimpleRouter

from .views import AccountViewSet

__all__ = ['urlpatterns']

app_name = 'account_api'

userRouter = SimpleRouter()

userRouter.register(r'accounts', viewset=AccountViewSet, basename='account')

urlpatterns = userRouter.urls
