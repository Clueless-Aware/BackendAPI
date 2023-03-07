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

    class Meta:
        model = Request
        fields = '__all__'

    def create(self, validated_data):
        request = Request.objects.create(**validated_data)
        request.save()

        send_mail(request.subject,
                  request.content,
                  request.from_user,
                  ['admin@webmaster'],
                  fail_silently=False)

        return request
