import os

from django.db import models

__all__ = ['Artwork', 'Artist']


# Create your models here.
def upload_to(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return 'images/artworks/{filename}'.format(filename=instance.id) + file_extension


def upload_to_artist(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return 'images/artists/{filename}'.format(filename=instance.name) + file_extension


class Artist(models.Model):
    name = models.CharField(max_length=50, db_column='artist', unique=True)
    birth_data = models.CharField(max_length=128, db_column='birth data')
    profession = models.CharField(max_length=50)
    # Italian, French, German, Flemish, ecc...
    school = models.CharField(max_length=50)

    # Biography
    biography = models.TextField(db_column='description', null=True)
    portrait = models.ImageField(upload_to=upload_to, max_length=64)

    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return f'{self.name} - {self.id}'


class Artwork(models.Model):
    # No primary key is specified

    # Can't use name as foreign key since some artists are unknown
    author = models.CharField(max_length=64)
    author_id = models.ForeignKey(to=Artist, on_delete=models.CASCADE)

    title = models.CharField(max_length=128)

    date = models.CharField(max_length=128)

    # Technique used like Oil on wood, Pen and ink, Cartoon, ecc...
    # This could also become a choice field
    technique = models.CharField(max_length=256)

    # Where the art is currently stored
    # This could be made into another model
    location = models.CharField(max_length=128)

    # Form of the artwork as in: painting, tapestry, graphics, architecture, ecc...
    form = models.CharField(max_length=50)

    # Type of artwork: Study, religious, portrait, fresco...
    # Could become a choice field
    type = models.CharField(max_length=50)

    # timeframe where the art was finalized, examples: 1501-1550, 1701-1750, 1551-1500, ecc...
    timeframe = models.CharField(max_length=50)

    description = models.TextField(null=True)

    image_url = models.ImageField(upload_to=upload_to, max_length=254, db_column='jpg url')

    def __str__(self):
        return self.title
