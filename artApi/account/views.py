from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Account, Favorite
from .serializers import AccountSerializer, FavoriteSerializer

__all__ = ['AccountViewSet', 'FavoriteViewSet']


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.order_by('owner_id')
    serializer_class = AccountSerializer
    parser_classes = (MultiPartParser, FormParser)

    # Permissions
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method in ['GET', 'OPTIONS']:
            return [permissions.AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


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
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method in ['GET', 'OPTIONS']:
            return [permissions.AllowAny()]
        return super().get_permissions()
