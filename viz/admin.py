from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Owner)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(UserAlbum)