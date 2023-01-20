from django.contrib import admin

from .models import User, Artwork

# Register your models here.

admin.site.register(User)
admin.site.register(Artwork)
