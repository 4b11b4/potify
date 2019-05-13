from django.db import models
from django.core.validators import FileExtensionValidator


class SongManager(models.Manager):
    def AlbumArtistPlaylist(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute("""
            SELECT s.id, s.artists, s.albums
            FROM models_song s
            GROUP BY s.id, s.artists, s.albums
            ORDER BY s.albums DESC""")
            result_list = []
            for row in cursor.fetchall():
                s = self.model(id=row[0], artists=row[1], albums=row[2])
                result_list.append(s)
        return result_list


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
    
    #objects = SongManager()
    #   ^ this line adds custom manager methods to the default manager?
    
    #   or, do we first need to define: 
    #   objects=ModelManager()    ..and, then..
    #   song_manager = SongManager()

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='./static/media/playlists')
    songs = models.ManyToManyField(Song, blank=True, related_name='playlists')

    def __str__(self):
        return self.name
