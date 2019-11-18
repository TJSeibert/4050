from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, default='title')
    category = models.CharField(max_length=20, default='Not Available')
    cast = models.TextField(default='cast')
    director = models.CharField(max_length=25, default='None')
    producer = models.CharField(max_length=25, default='None')
    rating = models.CharField(max_length=5, default='NR')
    poster = models.ImageField(default='default.jpg', upload_to='movie_posters')
    currentlyPlaying = models.BooleanField(default=False)
    synopsis = models.TextField(default='synopsis')
