from rest_framework import serializers

from .models import Artwork, Artist

__all__ = ['ArtworkSerializer', 'ArtistSerializer']


class ArtworkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    artist = serializers.CharField()
    title = serializers.CharField()
    picture_data = serializers.CharField()
    file_info = serializers.CharField()
    image_url = serializers.SerializerMethodField()

    def get_image_url(self, artwork):
        request = self.context.get('request')
        image_url = artwork.image_url.url
        return request.build_absolute_uri(image_url)

    class Meta:
        model = Artwork
        fields = '__all__'


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
        fields = '__all__'
