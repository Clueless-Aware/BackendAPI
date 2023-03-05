# Create your models here.
from artwork.models import Artwork, Artist
from django.contrib.auth.models import User, AbstractUser
from django.db import models

__all__ = ['Account', 'Favorite']


class ArtUser(AbstractUser):
    full_name = models.CharField(max_length=60, null=True)
    biography = models.TextField(null=True)
    favorite_artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username


class Account(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    full_name = models.CharField(max_length=60, null=True)
    biography = models.TextField(null=True)
    favorite_artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE, null=True)

    is_admin = models.BooleanField(default=False)


class Favorite(models.Model):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    artwork = models.ForeignKey(to=Artwork, on_delete=models.CASCADE)

    date = models.DateField()

    def __str__(self):
        return f'{self.account} - {self.artwork}'
