from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Flight
from .forms import FlightForm

# Create your views here.

def Home(request):
    template = loader.get_template('homePage.html')
    return HttpResponse(template.render())

def registerFlights(request):
    template = loader.get_template('registroVuelos.html')

    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['flightName']
            tipo = form.cleaned_data['flightType']
            precio = form.cleaned_data['flightPrice']
            p = Flight(nombre=nombre, tipo=tipo, precio=precio)
            p.save()

    else:
        form = FlightForm()

    context = {
        'form': form
    }
    return render(request, 'registroVuelos.html', context)

def listFlights(request):
    return HttpResponse("List Flights")

def flightStatistics(request):
    return HttpResponse("Flight Statistics")


