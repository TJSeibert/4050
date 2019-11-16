from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cinema-home'),
    path('browse/', views.browse, name='cinema-browse'),
]
