from artwork.models import Artwork
from django.core.mail import send_mail
from rest_framework import serializers
from users.models import User

from .models import Favorite, Request

__all__ = ['FavoriteSerializer', 'RequestSerializer']


class FavoriteSerializer(serializers.ModelSerializer):
    artwork = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Artwork.objects.all())
    account = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())

    class Meta:
        model = Favorite
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    from_user = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=User.objects.all())
    subject = serializers.CharField(max_length=64)
    content = serializers.CharField(required=False)
    critical = serializers.BooleanField(default=False)
    seen = serializers.BooleanField(default=False, read_only=True)

    class Meta:
        model = Request
        fields = '__all__'

    def create(self, validated_data):
        request = Request.objects.create(**validated_data)
        request.seen = False
        request.save()

        send_mail(request.subject,
                  request.content + f'\nOn {request.date}',
                  request.from_user.email,
                  ['admin@webmaster'],
                  fail_silently=False)

        return request


class RequestUpdateSerializer(serializers.ModelSerializer):
    from_user = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    subject = serializers.CharField(max_length=64, required=False)
    content = serializers.CharField(required=False)
    critical = serializers.BooleanField(default=False, required=False)
    seen = serializers.BooleanField(default=False, required=False)

    class Meta:
        model = Request
        fields = '__all__'

    def create(self, validated_data):
        request = Request.objects.create(**validated_data)
        request.save()
        return request


class UpdateDefaultSerializerMixin(object):
    default_serializer_class = None
    update_serializer_class = None

    def get_serializer_class(self):
        if self.action in ["update", "partial_update"]:
            return self.get_update_serializer_class()
        return self.get_default_serializer_class()

    def get_default_serializer_class(self):
        assert self.default_serializer_class is not None, (
                "'%s' should either include a `read_serializer_class` attribute,"
                "or override the `get_read_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.default_serializer_class

    def get_update_serializer_class(self):
        assert self.update_serializer_class is not None, (
                "'%s' should either include a `update_serializer_class` attribute,"
                "or override the `get_update_serializer_class()` method."
                % self.__class__.__name__
        )
        return self.update_serializer_class
