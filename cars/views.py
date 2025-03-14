from django.shortcuts import render
from cars.models import Car


def cars_views(request):

    print(request.GET.get('search'))

    cars = Car.objects.filter(model__icontains = 'a')

    context = {
    'cars': cars,
}

    return render(
        request,
        'cars.html',
        context,
    )
