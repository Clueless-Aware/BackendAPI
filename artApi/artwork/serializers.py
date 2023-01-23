from rest_framework import serializers

from .models import Artwork

__all__ = ['ArtworkSerializer']


class ArtworkSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    title = serializers.CharField(required=True)
    author = serializers.CharField(required=True)

    class Meta:
        model = Artwork
        fields = ('id', 'title', 'description', 'author', 'image_url')
