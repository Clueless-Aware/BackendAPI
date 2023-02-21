from django_filters import filters
from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Artwork
from .serializers import ArtworkSerializer

from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    parser_classes = (MultiPartParser, FormParser)
    #filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_fields = ['title', 'description']
    ordering_fields= '__all__'
    ordering = ['title']
    #permission
    permission_classes = [permissions.IsAdminUser]


    #permission
    def get_permissions(self):
        if self.request.method in ['GET','OPTIONS']:
            return [permissions.AllowAny()]
        return super().get_permissions()
