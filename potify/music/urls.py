from django.urls import path

from music import views

urlpatterns = [
    path('songs/', views.SongList.as_view(), name='song_list'),
    path('songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'),
    path('artists/', views.ArtistList.as_view(), name='artist_list'),
    path('artists/<int:pk>', views.ArtistDetail.as_view(), name='artist_detail'),
    path('albums/', views.AlbumList.as_view(), name='album_list'),
    path('albums/<int:pk>', views.AlbumDetail.as_view(), name='album_detail'),
    path('playlists/', views.PlaylistList.as_view(), name='playlist_list'),
    path('playlists/<int:pk>', views.PlaylistDetail.as_view(), name='playlist_detail'),
]
