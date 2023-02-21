import os

from django.db import models

__all__ = ['Artwork', 'Artist']


# Create your models here.
def upload_to(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return 'images/artworks/{filename}'.format(filename=instance.title) + file_extension


class Artwork(models.Model):
    title = models.CharField(
        max_length=80, blank=False, null=False)
    description = models.TextField()
    author = models.CharField(max_length=80, blank=False, null=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)


class Artist(models.Model):
    name = models.CharField(max_length=50, db_column='artist', primary_key=True)
    years = models.CharField(max_length=50, db_column='born-died')
    period = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    base = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    sourcePage = models.CharField(max_length=64, db_column='url')
