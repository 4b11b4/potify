from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from .models import Song
from .models import Artist 
from .models import Album 
from .models import Playlist 

# Create your views here.

class HomePageView(TemplateView):
    template_name = "base.html"


class SongList(ListView):
    model = Song


class ArtistList(ListView):
    model = Artist


class AlbumList(ListView):
    model = Album 


class PlaylistList(ListView):
    model = Playlist 
