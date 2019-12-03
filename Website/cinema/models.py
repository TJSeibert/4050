from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
import datetime


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, default='title', unique=True)
    category = models.CharField(max_length=20, default='Not Available')
    cast = models.TextField(default='cast')
    director = models.CharField(max_length=25, default='None')
    producer = models.CharField(max_length=25, default='None')
    rating = models.CharField(max_length=5, default='NR')
    poster = models.ImageField(default='default.jpg', upload_to='movie_posters')
    currentlyPlaying = models.BooleanField(default=False)
    synopsis = models.TextField(default='synopsis')
    trailer = models.FileField(upload_to='videos', null=True, verbose_name="")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.poster.path)

        if img.height > 480 or img.width > 320:
            output_size = (480, 320)
            img.thumbnail(output_size)
            img.save(self.poster.path)


class Showroom(models.Model):
    showroom_id = models.IntegerField(primary_key=True)
    numSeats = models.IntegerField()


class Show(models.Model):
    show_id = models.IntegerField(primary_key=True)
    showroom_id = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    showroom_name = models.IntegerField(default=0)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    movie_name = models.CharField(max_length=25, default='None')
    scheduledTime = models.TimeField()

    class Meta:
        unique_together = [("showroom_id", "scheduledTime")]


class seatInShowTime(models.Model):
    seatNumber = models.IntegerField(primary_key=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
    show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
    seatOccupied = models.BooleanField(default=False)


class Promotion(models.Model):
    promoID = models.IntegerField(primary_key=True)
