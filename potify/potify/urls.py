"""
potify URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from music.views import HomePageView


urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('', include('music.urls')),
]
