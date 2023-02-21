from rest_framework import serializers

from .models import Artwork, Artist

__all__ = ['ArtworkSerializer', 'ArtistSerializer']


class ArtworkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    artist = serializers.CharField()
    title = serializers.CharField()
    picture_data = serializers.CharField()
    file_info = serializers.CharField()
    image_url = serializers.CharField()

    class Meta:
        model = Artwork
        fields = ('id', 'artist', 'title',
                  'picture_data', 'file_info', 'image_url')


class ArtistSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
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
