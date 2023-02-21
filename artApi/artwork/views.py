from rest_framework import permissions, viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from .models import Artist, Artwork
from .serializers import ArtistSerializer, ArtworkSerializer


# Create your views here.
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.order_by('id')
    serializer_class = ArtworkSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method in ['GET', 'OPTIONS']:
            return [permissions.AllowAny()]
        return super().get_permissions()


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.order_by('name')
    serializer_class = ArtistSerializer
    parser_classes = (MultiPartParser, FormParser)
    permissions_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method in ['GET', 'OPTIONS']:
            return [permissions.AllowAny()]
        return super().get_permissions()
