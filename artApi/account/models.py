# Create your models here.
from artwork.models import Artwork
from django.conf import settings
from django.db import models
from users.models import User

__all__ = ['Favorite', 'Request']


class Favorite(models.Model):
    account = models.ForeignKey(to=User, on_delete=models.CASCADE)
    artwork = models.ForeignKey(to=Artwork, on_delete=models.CASCADE)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.account} - {self.artwork}'


class Request(models.Model):
    from_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=64)
    content = models.TextField(null=True)
    critical = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject} from {self.from_user}'
