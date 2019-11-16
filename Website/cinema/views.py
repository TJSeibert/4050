from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'cinema/home.html')


def browse(request):
    return render(request, 'cinema/browse.html')
