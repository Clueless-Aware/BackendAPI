from django.db import models


# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Artwork(models.Model):
    title = models.CharField(
        max_length=80, blank=False, null=False)
    description = models.TextField()
    author = models.CharField(max_length=80, blank=False, null=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
