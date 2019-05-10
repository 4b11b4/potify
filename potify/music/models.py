from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='./static/media/artists')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=255)
    release_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='./static/media/albums')
    description = models.TextField(blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist, blank=True, related_name='songs')
    albums = models.ManyToManyField(Album, blank=True, related_name='songs')
    audio = models.FileField(upload_to='songs',
		             help_text='Allowed format - .mp3',
			     validators=[FileExtensionValidator(allowed_extensions=['mp3'])],
			     null=True)
    play_count = models.IntegerField()

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='./static/media/playlists')
    songs = models.ManyToManyField(Song, blank=True, related_name='playlists')

    def __str__(self):
        return self.name
