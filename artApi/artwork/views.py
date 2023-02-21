from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Artwork
from .serializers import ArtworkSerializer


# Create your views here.
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.order_by('title')
    serializer_class = ArtworkSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method in ['GET','OPTIONS']:
            return [permissions.AllowAny()]
        return super().get_permissions()
