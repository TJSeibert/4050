from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
import datetime
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

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


class Showroom(models.Model):
    showroom_id = models.IntegerField(primary_key=True)
    numSeats = models.IntegerField()

class Show(models.Model):
    show_id = models.IntegerField(primary_key=True)
    showroom_id = models.ForeignKey(Showroom, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    scheduledTime = models.TimeField()


class seatInShowTime(models.Model):
   seatNumber = models.IntegerField(primary_key=True, validators=[MinValueValidator(0), MaxValueValidator(30)])
   show_id = models.ForeignKey(Show, on_delete=models.CASCADE)
   seatOccupied = models.BooleanField(default=False)

class Promotion(models.Model):
    promoID = models.IntegerField(primary_key=True)

class Ticket(models.Model):
    ticketID = models.IntegerField(primary_key=True)
    age = (
        ('Child', 'Child'),
        ('Adult', 'Adult'),
        ('Senior', 'Senior'),
        )
    ageType = models.CharField(max_length = 100, choices = age)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def setPrice(sender, **kwargs):
        if age == 'Child':
            price = 8.00
        elif age == 'Adult':
            price = 10.00
        else:
            price = 12.00

    




