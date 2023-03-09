from allauth.account.adapter import get_adapter
from artwork.models import Artist, Artwork
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    favorite_artist = serializers.PrimaryKeyRelatedField(many=False, read_only=False,
                                                         queryset=Artist.objects.all(), required=False)
    profile_picture = serializers.ImageField(required=False)

    user_favorites = serializers.HyperlinkedRelatedField(many=True, view_name='accounts:favorite-detail',
                                                         queryset=Artwork.objects.all(), lookup_field='pk')

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

    def get_profile_picture(self, user):
        request = self.context.get('request')
        profile_pic_url = user.profile_picture.url
        return request.build_absolute_uri(profile_pic_url)


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    favorite_artist = serializers.PrimaryKeyRelatedField(many=False, read_only=False,
                                                         queryset=Artist.objects.all(), required=False)
    biography = serializers.CharField(required=False)
    profile_picture = serializers.ImageField(required=False)
    email = serializers.EmailField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'favorite_artist': self.validated_data.get('favorite_artist'),
            'biography': self.validated_data.get('biography'),
            'profile_picture': self.validated_data.get('profile_picture'),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()

        user.favorite_artist = self.cleaned_data.get('favorite_artist')
        user.biography = self.cleaned_data.get('biography')
        if self.cleaned_data.get('profile_picture') is not None:
            user.profile_picture = self.cleaned_data.get('profile_picture')

        # Users created via register serializer can't be admin
        user.is_staff = False
        user.is_superuser = False
        user.is_active = True

        user.save()
        adapter.save_user(request, user, self)
        return user

    class Meta:
        model = User
        fields = '__all__'

    def get_profile_picture(self, user):
        request = self.context.get('request')
        profile_pic_url = user.profile_picture.url
        return request.build_absolute_uri(profile_pic_url)
