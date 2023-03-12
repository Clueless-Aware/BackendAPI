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

    # Form of the artwork as in: painting, tapestry, graphics, architecture, ecc...
    form = serializers.CharField()
    # Type of artwork: Study, religious, portrait, fresco...
    type = serializers.CharField()
    timeframe = serializers.CharField()
    description = serializers.CharField(required=False)

    image_url = serializers.ImageField(required=False)

    # users = serializers.ManyRelatedField(source='favorites_artworks')

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
    # Artist portrait
    portrait = serializers.ImageField()

    def get_portrait(self, artist):
        request = self.context.get('request')
        portrait_url = artist.portrait.url
        return request.build_absolute_uri(portrait_url)

    class Meta:
        model = Artist
        fields = '__all__'
