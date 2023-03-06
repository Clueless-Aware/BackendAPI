from artwork.models import Artwork
from rest_framework import serializers
from users.models import User

from .models import Favorite

__all__ = ['FavoriteSerializer']


class FavoriteSerializer(serializers.ModelSerializer):
    artwork = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Artwork.objects.all())
    account = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())

    date = serializers.DateField()

    class Meta:
        model = Favorite
        fields = '__all__'
