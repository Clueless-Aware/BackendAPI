# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    owner = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=60)


class Favorite(models.Model):
    account = models.ForeignKey(to=Account, on_delete=models.CASCADE)
