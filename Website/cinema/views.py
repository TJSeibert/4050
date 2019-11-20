from django.shortcuts import render
from django.http import HttpResponse
from . models import Movie


def home(request):
    allmovies = Movie.objects.all()
    context = {
        'allmovies': allmovies
    }
    return render(request, 'cinema/home.html', context)


def browse(request):
    return render(request, 'cinema/browse.html')
