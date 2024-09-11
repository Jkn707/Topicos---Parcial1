from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('registerFlights/', views.registerFlights, name='registerFlights'),
    path('listFlights/', views.listFlights, name='listFlights'),
    path('flightStatistics/', views.flightStatistics, name='flightStatistics'),
]
