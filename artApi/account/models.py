# Create your models here.
from artwork.models import Artwork
from django.db import models
from users.models import User

__all__ = ['Favorite']


class Favorite(models.Model):
    account = models.ForeignKey(to=User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(to=Artwork, on_delete=models.CASCADE)

    date = models.DateField()

    def __str__(self):
        return f'{self.account} - {self.artwork}'
