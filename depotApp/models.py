from django.db import models

# Create your models here.


class artist(models.Model):
    name = models.CharField(max_length=128)


class song(models.Model):
    title = models.CharField(max_length=128)
    artists = models.CharField(max_length=128)

class album(models.Model):
    title = models.CharField(max_length=128)
    