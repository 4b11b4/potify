from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from .models import Song

# Create your views here.

class HomePageView(TemplateView):
    template_name = "base.html"

class SongList(ListView):
    model = Song
