import os

from artwork.models import Artist
from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = ['User']


# This somehow doesn't work... I AM AT WITS END
def upload_to_user(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return f'images/users/{instance.get_username()}' + file_extension


class User(AbstractUser):
    biography = models.TextField(null=True)
    favorite_artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to='images/users/', max_length=256,
                                        default='images/users/default/unknown.jpg')

    def __str__(self):
        return f'{self.username} - {self.email}'
