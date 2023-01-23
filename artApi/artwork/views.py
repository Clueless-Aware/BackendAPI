from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Artwork
from .serializers import ArtworkSerializer


# Create your views here.
class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.order_by('-creation_date')
    serializer_class = ArtworkSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    # todo : Ask Kevin
    # def perform_create(self, serializer):
    #    serializer.save(creator=self.request.user)
