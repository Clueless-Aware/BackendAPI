from rest_framework import serializers

from .models import Account

__all__ = ['AccountSerializer']


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = Account
        fields = ('owner_id', 'owner', 'first_name', 'last_name')
