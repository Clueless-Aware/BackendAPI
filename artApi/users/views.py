from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser

from .models import User, Bookmark
from .serializers import UserSerializer, BookmarkSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser, FormParser)

    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    search_fields = ['username', 'favorite_artist']
    filterset_fields = ['username', 'favorite_artist']
    ordering_fields = '__all__'
    ordering = ['id']

    # Permissions
    permission_classes = [permissions.IsAdminUser]

    def get_permissions(self):
        return super().get_permissions()


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    # Filtering
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

    search_fields = ['user', 'artwork', 'date']
    filterset_fields = ['user', 'artwork', 'date']
    ordering_fields = '__all__'
    ordering = ['date']

    # Permissions
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        return super().get_permissions()
