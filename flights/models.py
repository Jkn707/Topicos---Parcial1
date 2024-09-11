from django.db import models
from django.forms import ModelForm

# Create your models here.

FLIGHT_TYPE_CHOICES = (
    ('Nacional', 'Nacional'),
    ('Internacional', 'Internacional'),
)

class Flight(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, choices=FLIGHT_TYPE_CHOICES)
    precio = models.IntegerField()


class FlightForm(ModelForm):
    class Meta:
        model = Flight
        fields = ['nombre', 'tipo', 'precio']

        