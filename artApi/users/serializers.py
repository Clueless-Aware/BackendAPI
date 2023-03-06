from artwork.models import Artist
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    favorite_artist = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Artist.objects.all())

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        # Users created via serializer can't be admins
        user.is_staff = False
        user.is_superuser = False
        user.set_password(validated_data['password'])
        user.save()
        return user
