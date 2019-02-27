from django.urls import path
from music.views import SongList
from music.views import ArtistList
from music.views import AlbumList
from music.views import PlaylistList

urlpatterns = [
    path('songs/', SongList.as_view(), name='song_list'),
    path('artists/', ArtistList.as_view(), name='artist_list'),
    path('albums/', AlbumList.as_view(), name='album_list'),
    path('playlists/', PlaylistList.as_view(), name='playlist_list'),
]
