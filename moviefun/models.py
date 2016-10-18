from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(default=1900)
    cast = models.CharField(max_length=200)
    rating = models.FloatField(default=0.0)
    genre = models.CharField(max_length=200)
    cover = models.CharField(max_length=200)
    director = models.CharField(max_length=200)

class Loc(models.Model):
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

class MovieLocR(models.Model):
    loc_id = models.ForeignKey(Movie, related_name='loc_id', on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, related_name='movie_id', on_delete=models.CASCADE)

class RecomR(models.Model):
    movie1_id = models.ForeignKey(Movie, related_name='movie1_id', on_delete=models.CASCADE)
    movie2_id = models.ForeignKey(Movie, related_name='movie2_id', on_delete=models.CASCADE)

class TVPlay(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    time = models.DateTimeField()
    season_number = models.IntegerField(default=0)
    episode_number = models.IntegerField(default=0)

# Create your models here.
