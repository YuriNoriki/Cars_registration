from django.shortcuts import render
from cars.models import Car
from cars.forms import CarForm


def cars_views(request):
    # Primeiro buscou todos os carros
    cars = Car.objects.all().order_by('model')
    # Verifica se o usuario mandou alguma busca
    search = request.GET.get('search') 
    # Se mandou,
    if search:
        #cars. filter vai filtrar os carros que ja mandou buscar(cars = Car.objects.all)
        cars = cars.filter(model__contains = search)
        
        
    context = {
    'cars': cars,
    }

    return render(
        request,
        'cars.html',
        context,
    )

def new_cars_views(request):
    new_cars_form = CarForm()

    context = {
        'new_cars_form': new_cars_form,
    }

    return render(
        request,
        'new_cars.html',
        context,
    )