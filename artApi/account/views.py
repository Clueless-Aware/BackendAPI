from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination

from .models import Request
from .serializers import RequestSerializer, UpdateDefaultSerializerMixin, RequestUpdateSerializer

__all__ = ['RequestViewSet']


class RequestPagination(PageNumberPagination):
    page_size = 10000
    page_size_query_param = 'page_size'
    max_page_size = 10000


class RequestViewSet(UpdateDefaultSerializerMixin, viewsets.ModelViewSet):
    queryset = Request.objects.all()
    default_serializer_class = RequestSerializer
    update_serializer_class = RequestUpdateSerializer

    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    search_fields = ['from_user', 'subject', 'content', 'critical', 'date']
    filterset_fields = ['from_user', 'subject', 'content', 'critical', 'date']
    ordering_fields = '__all__'
    ordering = ['date']

    # Permissions
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        # if self.request.method in ['GET', 'OPTIONS']:
        #    return [permissions.IsAdminUser()]
        return super().get_permissions()
