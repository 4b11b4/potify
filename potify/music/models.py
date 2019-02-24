from django.db import models

# Create your models here.

class Song(models.Model):
    title = models.CharField(max_length=100)
    #audio = 
    play_count = models.IntegerField()

    def __str__(self):
        return self.title
