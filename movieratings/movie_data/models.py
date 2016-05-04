from django.db import models

class Movie(models.Model):
    movie_id = model.IntegerField(default=0)
    movie = model.CharField(max_length=200)
    release_date = model.DatetimeField()
    video_release_date = model.DatetimeField()
    IMDb_url = model.CharField(max_length=200)

class Rater(models.Model):
    rater_id = model.IntegerField(default=0)
    age = model.IntegerField(default=0)
    gender = model.CharField(max_length=2)
    occupation = model.CharField(max_length=30)
    zipcode = model.IntegerField(default=0)

class Rating(models.Model):
    rater_id = model.ForeignKey(Rater)
    movie_id = model.ForeignKey(Movie)
    rating = model.IntegerField(default=0)
    timestamp = model.IntegerField(default=0)
