from django.contrib import admin

from .models import Favorite, Request

# Register your models here.

admin.site.register(Favorite)
admin.site.register(Request)
