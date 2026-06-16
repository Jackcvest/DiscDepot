from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=128)

    primary_artist = models.ForeignKey(  #primary_artist is used as a way to simplify db relationships given most songs have only 1 artist
        Artist,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        related_name='primary_songs' #defines the reverse action, eg. using artistname.primary_songs.all() would allow access to all songs primarily attributed to artistname
    )

    artists = models.ManyToManyField(
        Artist,
        related_name='song_credits'
        )

    duration = models.DurationField(
        null=False, 
        blank=False
        )

    album = models.ForeignKey(
        'Album', 
        related_name='songs', 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
        )

    release_date = models.DateField()

    def __str__(self):
        return self.title

class Album(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title
    