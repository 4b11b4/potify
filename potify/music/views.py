from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
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


class SongDetail(DetailView):
    model = Song

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ArtistList(ListView):
    model = Artist


class ArtistDetail(DetailView):
    model = Artist


class AlbumList(ListView):
    model = Album 


class AlbumDetail(DetailView):
    model = Album 


class PlaylistList(ListView):
    model = Playlist 


class PlaylistDetail(DetailView):
    model = Playlist
    

