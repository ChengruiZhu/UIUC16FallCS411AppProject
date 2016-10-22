from django.db import models

class Movie(models.Model):
    imdbid = models.CharField(primary_key=True, max_length=200)
    title = models.CharField(max_length=200, default='N/A')
    year = models.CharField(max_length=200, default='N/A')
    rated = models.CharField(max_length=200, default='N/A')
    released = models.CharField(max_length=200, default='N/A')
    runtime = models.CharField(max_length=200, default='N/A')
    genre = models.CharField(max_length=200, default='N/A')
    director = models.CharField(max_length=200, default='N/A')
    writer = models.CharField(max_length=200, default='N/A')
    actors = models.CharField(max_length=200, default='N/A')
    plot = models.CharField(max_length=500, default='N/A')
    language = models.CharField(max_length=200, default='N/A')
    awards = models.CharField(max_length=200, default='N/A')
    poster = models.CharField(max_length=200, default='N/A')
    imdbrating = models.CharField(max_length=200, default='N/A')
    imdbvotes = models.CharField(max_length=200, default='N/A')
    type = models.CharField(max_length=200, default='N/A')

class Loc(models.Model):
    address = models.CharField(primary_key=True, max_length=200)
    longitude = models.CharField(max_length=200, default='N/A')
    latitude = models.CharField(max_length=200, default='N/A')

class MovieLocR(models.Model):
    address = models.ForeignKey(Loc, on_delete=models.CASCADE)
    imdbid = models.OneToOne(Movie, on_delete=models.CASCADE, primary_key=True)

class RecomR(models.Model):
    movie1_id = models.ForeignKey(Movie, related_name='movie1_id', on_delete=models.CASCADE)
    movie2_id = models.ForeignKey(Movie, related_name='movie2_id', on_delete=models.CASCADE)

class TVPlay(models.Model):
    imdbid = models.OneToOneField(Movie, on_delete=models.CASCADE, primary_key=True)
    season = models.CharField(max_length=200, default='N/A')
    episode = models.CharField(max_length=200, default='N/A')
    seriesid = models.CharField(max_length=200, default='N/A')

class TVSeries(models.Model):
    seriesid = models.OneToOneField(Movie, on_delete=models.CASCADE, primary_key=True)
    totalseasons = models.CharField(max_length=200, default='N/A')
    ##
# Create your models here.
