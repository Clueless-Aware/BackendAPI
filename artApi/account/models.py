# Create your models here.
from artwork.models import Artwork
from django.contrib.auth.models import User
from django.db import models

__all__ = ['Account', 'Favorite']


class Account(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    full_name = models.CharField(max_length=60)
    biography = models.TextField()
    email = models.EmailField()


class Favorite(models.Model):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    artwork = models.ForeignKey(to=Artwork, on_delete=models.CASCADE)

    date = models.DateTimeField()
