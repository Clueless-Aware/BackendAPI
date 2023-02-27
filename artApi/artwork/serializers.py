from rest_framework import serializers

from .models import Artwork, Artist

__all__ = ['ArtworkSerializer', 'ArtistSerializer']


class ArtworkSerializer(serializers.ModelSerializer):
    # Author info
    author = serializers.CharField()
    author_id = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=Artist.objects.all())

    title = serializers.CharField()
    # Image Info
    date = serializers.CharField()
    technique = serializers.CharField()
    location = serializers.CharField()

    # File info
    form = serializers.CharField()
    type = serializers.CharField()
    timeframe = serializers.CharField()
    description = serializers.CharField()

    image_url = serializers.ImageField()

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
    portrait = serializers.ImageField()

    id = serializers.IntegerField()

    def get_portrait(self, artist):
        request = self.context.get('request')
        portrait_url = artist.portrait.url
        return request.build_absolute_uri(portrait_url)

    class Meta:
        model = Artist
        fields = '__all__'
