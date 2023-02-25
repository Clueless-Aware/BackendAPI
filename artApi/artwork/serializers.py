from rest_framework import serializers

from .models import Artwork, Artist

__all__ = ['ArtworkSerializer', 'ArtistSerializer']


class ArtworkSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    author = serializers.CharField()
    title = serializers.CharField()
    # Image Info
    resolution = serializers.CharField()
    color = serializers.CharField()
    file_dimension = serializers.CharField()
    # File info
    date = serializers.CharField()
    type = serializers.CharField()
    size = serializers.CharField()
    museum = serializers.CharField()

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
    birth_data = serializers.CharField()
    profession = serializers.CharField()
    school = serializers.CharField()

    # Biography
    biography = serializers.CharField()
    portrait = serializers.CharField()

    class Meta:
        model = Artist
        fields = '__all__'
