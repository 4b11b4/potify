from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from rest_framework import viewsets

from .models import Song, Artist, Album, Playlist
from .serializers import SongSerializer, ArtistSerializer, AlbumSerializer, PlaylistSerializer


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


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ArtistList(ListView):
    model = Artist


class ArtistDetail(DetailView):
    model = Artist


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class AlbumList(ListView):
    model = Album


class AlbumDetail(DetailView):
    model = Album


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PlaylistList(ListView):
    model = Playlist


class PlaylistDetail(DetailView):
    model = Playlist


class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
