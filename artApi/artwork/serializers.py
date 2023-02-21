from rest_framework import serializers

from .models import Artwork, Artist

__all__ = ['ArtworkSerializer', 'ArtistSerializer']


class ArtworkSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    title = serializers.CharField(required=True)
    author = serializers.CharField(required=True)

    class Meta:
        model = Artwork
        fields = ('id', 'title', 'description', 'author', 'image_url')


class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    years = serializers.CharField()
    period = serializers.CharField()
    school = serializers.CharField()
    base = serializers.CharField()
    nationality = serializers.CharField()
    sourcePage = serializers.CharField()

    class Meta:
        model = Artist
        fields = ('name', 'years', 'period', 'school',
                  'base', 'nationality', 'sourcePage')
