from artwork.models import Artwork
from rest_framework import serializers

from .models import Account, Favorite

__all__ = ['AccountSerializer', 'FavoriteSerializer']


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = Account
        fields = ('owner_id', 'owner', 'first_name', 'last_name')


class FavoriteSerializer(serializers.ModelSerializer):
    artwork = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Artwork.objects.all())
    account = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Account.objects.all())

    date = serializers.DateField()

    class Meta:
        model = Favorite
        fields = '__all__'
