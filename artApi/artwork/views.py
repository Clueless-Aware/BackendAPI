from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Artist, Artwork
from .serializers import ArtistSerializer, ArtworkSerializer

__all__ = ['ArtworkViewSet', 'ArtistViewSet']


class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    parser_classes = (MultiPartParser, FormParser)

    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    search_fields = ['title', 'author', 'technique',
                     'location', 'timeframe', 'form', 'type']
    filterset_fields = ['title', 'author', 'technique',
                        'location', 'timeframe', 'form', 'type', 'author_id', 'id']
    ordering_fields = '__all__'
    ordering = ['id']

    # Permissions
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method in ['GET', 'OPTIONS']:
            return [permissions.AllowAny()]
        return super().get_permissions()


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    parser_classes = (MultiPartParser, FormParser)

    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    search_fields = ['name', 'birth_data', 'profession', 'school']
    filterset_fields = ['name', 'birth_data', 'profession', 'school', 'id']
    ordering_fields = '__all__'
    ordering = ['name']

    # Permissions
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method in ['GET', 'OPTIONS']:
            return [permissions.AllowAny()]
        return super().get_permissions()
