from artwork.models import Artist
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    favorite_artist = serializers.PrimaryKeyRelatedField(many=False, read_only=False,
                                                         queryset=Artist.objects.all(), required=False)

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        # Users created via serializer can't be admins
        user.is_staff = False
        user.is_superuser = False
        user.is_active = True

        user.set_password(validated_data['password'])
        user.save()
        return user


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    favorite_artist = serializers.PrimaryKeyRelatedField(many=False, read_only=False,
                                                         queryset=Artist.objects.all(), required=False)
    biography = serializers.CharField(required=False)

    def get_cleaned_data(self):
        print('Getting cleaned data :)')
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'favorite_artist': self.validated_data.get('favorite_artist', ''),
            'biography': self.validated_data.get('biography', ''),

            # Users by default are created as normal user
            'is_staff': False,
            'is_superuser': False,
            'is_active': True,
        }
