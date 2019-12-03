from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from . models import Movie, Show, Showroom, seatInShowTime
from django.db.models import Q


def home(request):
    allmovies = Movie.objects.all()
    context = {
        'allmovies': allmovies
    }
    return render(request, 'cinema/home.html', context)


def browse(request):
    if request.GET:
        query = request.GET['q']
        submitbutton = request.GET.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query) | Q(category__icontains=query)
            results = Movie.objects.filter(lookups).distinct()
            context = {'results': results,
                       'submitbutton': submitbutton}
            return render(request, 'cinema/browse.html', context)

        else:
            return render(request, 'cinema/browse.html')
    else:
        return render(request, 'cinema/browse.html')


class MovieDetailView(DetailView):
    model = Movie


class ShowtimesListView(ListView):
    model = Show
