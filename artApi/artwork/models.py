import os

from django.db import models


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
