from django.db import models
from PIL import Image


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.poster.path)

        if img.height > 480 or img.width > 320:
            output_size = (480, 320)
            img.thumbnail(output_size)
            img.save(self.poster.path)
