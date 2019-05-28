"""
potify URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from music.views import HomePageView
from rest_framework import routers

from music import views

from .views import index, simple_api_view


router = routers.DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'playlists', views.PlaylistViewSet)

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view()),
    path('', include('music.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('api/phrases/', simple_api_view, name='phrases'),
]
