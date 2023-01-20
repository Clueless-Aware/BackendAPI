from django.db import models


class User(models.Model):
    Username = models.CharField(max_length=30)
    Email = models.CharField(max_length=50)
