from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='cinema-home'),
    path(r'browse/^$', views.browse, name='cinema-browse'),
    path('browse/movie/<int:pk>/', views.MovieDetailView.as_view(), name='detail'),
    path('shows/', views.ShowtimesListView.as_view(), name='show-list'),
]
