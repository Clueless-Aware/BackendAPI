from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Favorite, Request
from .serializers import FavoriteSerializer, RequestSerializer, UpdateDefaultSerializerMixin, RequestUpdateSerializer

__all__ = ['FavoriteViewSet', 'RequestViewSet']


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    search_fields = ['artwork', 'account', 'date']
    filterset_fields = ['artwork', 'account', 'date']
    ordering_fields = '__all__'
    ordering = ['date']

    # Permissions
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        return super().get_permissions()


class RequestViewSet(UpdateDefaultSerializerMixin, viewsets.ModelViewSet):
    queryset = Request.objects.all()
    default_serializer_class = RequestSerializer
    update_serializer_class = RequestUpdateSerializer

    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    search_fields = ['from_user', 'subject', 'content', 'critical', 'date']
    filterset_fields = ['from_user', 'subject', 'content', 'critical', 'date']
    ordering_fields = '__all__'
    ordering = ['date']

    # Permissions
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        # if self.request.method in ['GET', 'OPTIONS']:
        #    return [permissions.IsAdminUser()]
        return super().get_permissions()
