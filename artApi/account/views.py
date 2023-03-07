from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Favorite, Request
from .serializers import FavoriteSerializer, RequestSerializer

__all__ = ['FavoriteViewSet', 'RequestViewSet']


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    parser_classes = (MultiPartParser, FormParser)

    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    search_fields = ['artwork', 'account', 'date']
    filterset_fields = ['artwork', 'account', 'date']
    ordering_fields = '__all__'
    ordering = ['date']

    # Permissions
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['GET', 'OPTIONS']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    parser_classes = (MultiPartParser, FormParser)

    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    search_fields = ['from_user', 'subject', 'content', 'critical', 'date']
    filterset_fields = ['from_user', 'subject', 'content', 'critical', 'date']
    ordering_fields = '__all__'
    ordering = ['date']

    # Permissions
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ['GET', 'OPTIONS']:
            return [permissions.IsAdminUser()]
        return super().get_permissions()
