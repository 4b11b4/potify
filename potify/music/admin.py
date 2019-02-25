from django.contrib import admin

# Register your models here.

from .models import Song
from .models import Artist
from .models import Album
from .models import Playlist
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Playlist)
