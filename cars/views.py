from django.shortcuts import render
from cars.models import Car


def cars_views(request):
    # Primeiro buscou todos os carros
    cars = Car.objects.all()
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
