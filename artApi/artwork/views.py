from django_filters import filters
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Artist, Artwork
from .serializers import ArtistSerializer, ArtworkSerializer

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    parser_classes = (MultiPartParser, FormParser)
    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_fields = ['title', 'description']
    ordering_fields= '__all__'
    ordering = ['title']
    # Permission
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
        filter_backends = (DjangoFilterBackend, OrderingFilter,)
        filterset_fields = ['title', 'description']
        ordering_fields = '__all__'
        ordering = ['name']
        # Permission
        permissions_classes = [permissions.IsAdminUser]

        def get_permissions(self):
            if self.request.method in ['GET', 'OPTIONS']:
                return [permissions.AllowAny()]
            return super().get_permissions()

