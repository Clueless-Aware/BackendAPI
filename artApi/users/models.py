import os

from artwork.models import Artist
from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = ['User']


def upload_to(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return 'images/users/{filename}'.format(filename=instance.username) + file_extension


class User(AbstractUser):
    biography = models.TextField(null=True)
    favorite_artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.username
