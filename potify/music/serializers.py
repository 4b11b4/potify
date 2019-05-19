from .models import Album, Artist, Song, Playlist
from rest_framework import serializers


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
        exclude = ()


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        exclude = ()


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        exclude = ()


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Playlist
        exclude = ()
