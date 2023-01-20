from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=50)


class Artwork(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50, blank=True)
    path_to_image = models.CharField(max_length=100)
