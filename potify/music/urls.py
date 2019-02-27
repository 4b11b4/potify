from django.urls import path
from music.views import SongList
from music.views import SongDetail
from music.views import ArtistList
from music.views import ArtistDetail
from music.views import AlbumList
from music.views import AlbumDetail
from music.views import PlaylistList
from music.views import PlaylistDetail

urlpatterns = [
    path('songs/', SongList.as_view(), name='song_list'),
    path('', SongDetail.as_view(), name='song_detail'),
    path('artists/', ArtistList.as_view(), name='artist_list'),
    #path('<slug:slug>/', ArtistDetail.as_view(), name='artist_detail'),
    path('albums/', AlbumList.as_view(), name='album_list'),
    #path('<slug:slug>/', AlbumDetail.as_view(), name='album_detail'),
    path('playlists/', PlaylistList.as_view(), name='playlist_list'),
    #path('<slug:slug>/', PlaylistDetail.as_view(), name='playlist_detail'),
]
