from artwork.models import Artwork, Artist
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Account, Favorite

__all__ = ['AccountSerializer', 'FavoriteSerializer']


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=get_user_model().objects.all())
    is_admin = serializers.BooleanField()

    full_name = serializers.CharField()
    biography = serializers.CharField()
    favorite_artist = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Artist.objects.all())

    class Meta:
        model = Account
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    artwork = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Artwork.objects.all())
    account = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Account.objects.all())

    date = serializers.DateField()

    class Meta:
        model = Favorite
        fields = '__all__'
