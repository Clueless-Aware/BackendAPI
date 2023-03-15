# Create your models here.
from django.conf import settings
from django.db import models

__all__ = ['Request']


class Request(models.Model):
    from_user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_email_info')
    subject = models.CharField(max_length=64)
    content = models.TextField(null=True)
    critical = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)
    email = models.EmailField()

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.subject} from {self.from_user}'
