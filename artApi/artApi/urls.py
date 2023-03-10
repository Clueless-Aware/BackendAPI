"""artApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    # Documentation with swagger
    path('api/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui', SpectacularSwaggerView.as_view(url_name='schema'), name='swaggerUI'),
    # Url used to generate email content
    path('password-reset/confirm/<uidb64>/<token>/', TemplateView.as_view(), name='password_reset_confirm'),
    # Models view sets
    path('api/', include('artwork.urls', namespace='artworks')),
    path('api/', include('account.urls', namespace='accounts')),
    path('api/', include('users.urls', namespace='users')),
    # Auth
    path('api/auth/', include('dj_rest_auth.urls')),
    # Registration
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
]

# Media storage location
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
