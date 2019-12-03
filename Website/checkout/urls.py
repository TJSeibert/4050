from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart, name='checkout-cart'),
    path('info/', views.info, name='checkout-info'),
    path('finalize/', views.finalize, name='checkout-finalize')
]