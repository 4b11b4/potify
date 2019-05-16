from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .models import Song, Artist, Album, Playlist


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
