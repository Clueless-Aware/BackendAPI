from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Account
from .serializers import AccountSerializer

__all__ = ['AccountViewSet']


# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.order_by('-owner_id')
    serializer_class = AccountSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [
        # todo : change this to authenticated only
        permissions.AllowAny]

    # todo : Ask Kevin
    # def perform_create(self, serializer):
    #    serializer.save(creator=self.request.user)
