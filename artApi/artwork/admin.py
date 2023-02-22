from django.contrib import admin

from .models import Artwork, Artist

# Register your models here.

admin.site.register(Artwork)
admin.site.register(Artist)
