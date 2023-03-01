from django.contrib import admin

from .models import Account, Favorite

# Register your models here.

admin.site.register(Account)
admin.site.register(Favorite)
