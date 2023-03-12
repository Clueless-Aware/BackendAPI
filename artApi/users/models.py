import os

from artwork.models import Artwork, Artist
from django.contrib.auth.models import AbstractUser
from django.db import models

__all__ = ['User', 'Bookmark']


# This somehow doesn't work... I AM AT WITS END
def upload_to_user(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return f'images/users/{instance.get_username()}' + file_extension


class User(AbstractUser):
    biography = models.TextField(null=True)
    favorite_artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE, null=True)
    profile_picture = models.ImageField(upload_to='images/users/', max_length=256,
                                        default='images/users/default/unknown.jpg')
    bookmarked_artworks = models.ManyToManyField(Artwork, through='Bookmark', through_fields=('user', 'artwork'),
                                                 related_name='favorites_artworks', blank=True)

    def __str__(self):
        return f'{self.username} - {self.email}'


class Bookmark(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user_bookmarks')
    artwork = models.ForeignKey(to=Artwork, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'artwork'], name='unique_user_artwork_combination_bookmark'
            )
        ]

    def __str__(self):
        return f'{self.user} - {self.artwork}'
