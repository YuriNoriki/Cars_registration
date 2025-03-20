from django.shortcuts import render,redirect
from cars.models import Car
from cars.forms import  CarModelForm


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
    if request.method == 'POST':
        new_cars_form = CarModelForm(request.POST, request.FILES)
        if new_cars_form.is_valid():
            new_cars_form.save()
            return redirect('cars_list')
    else:
        new_cars_form = CarModelForm()

    context = {
        'new_cars_form': new_cars_form,
    }

    return render(
        request,
        'new_cars.html',
        context,
    )