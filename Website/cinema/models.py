from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
import datetime
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver


class Movie(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50, default='title', unique=True)
    category = models.CharField(max_length=20, default='Not Available')
    cast = models.TextField(default='cast')
    director = models.CharField(max_length=25, default='None')
    producer = models.CharField(max_length=25, default='None')
    rating = models.CharField(max_length=5, default='NR')
    poster = models.CharField(max_length=255)
    currentlyPlaying = models.BooleanField(default=False)
    synopsis = models.TextField(default='synopsis')
    trailer = models.CharField(max_length=255)


class Showroom(models.Model):
    seat_rows = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    seat_columns = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])

    def seat_num(self):
        return self.seat_rows.to_python() * self.seat_columns.to_python()


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
    status = (
        ('Empty', 'Empty'),
        ('Filled', 'Filled'),
        ('Pending', 'Pending'),
    )

    seatStatus = models.CharField(max_length=10, choices=status)


class Promotion(models.Model):
    amt = models.FloatField(default=0.5)
    code = models.CharField(max_length=24, default="promo")
    start = models.DateField()
    end = models.DateField()


class Ticket(models.Model):
    ticketID = models.IntegerField(primary_key=True)
    age = (
        ('Child', 'Child'),
        ('Adult', 'Adult'),
        ('Senior', 'Senior'),
    )
    ageType = models.CharField(max_length=100, choices=age)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def setPrice(sender, **kwargs):
        if age == 'Child':
            price = 8.00
        elif age == 'Adult':
            price = 10.00
        else:
            price = 12.00
