import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Artist(models.Model):
    foto = models.ImageField(upload_to="artist")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MusicGenre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MusicSubGenre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class MusicForDistribution(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('Tahun Release')
    genre = models.ForeignKey(MusicGenre, on_delete=models.CASCADE, null=True)
    subgenre = models.ForeignKey(
        MusicSubGenre, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.artist} - {self.title}"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
