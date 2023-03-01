from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Account
from .serializers import AccountSerializer

__all__ = ['AccountViewSet']


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
