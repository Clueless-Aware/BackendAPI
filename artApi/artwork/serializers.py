from rest_framework import serializers

from .models import Artwork

__all__ = ['ArtworkSerializer']


class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ('id', 'title', 'description', 'author', 'image_url')
