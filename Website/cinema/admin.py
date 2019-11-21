from django.contrib import admin
from . models import Movie
from . models import Showroom
from . models import Show
from . models import seatInShowTime

admin.site.register(Movie)
admin.site.register(Show)
admin.site.register(Showroom)
admin.site.register(seatInShowTime)