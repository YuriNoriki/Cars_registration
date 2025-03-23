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
        cars = cars.filter(model__icontains = search)


    #for car in cars:
        #print(f"Modelo: {car.model}, Ano: {car.factory_year}, Preço: {car.value}") 
        
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
        #print("Dados recebidos no POST:", request.POST)  # <-- Verifica os dados enviados
        
        new_cars_form = CarModelForm(request.POST, request.FILES)
        if new_cars_form.is_valid():
            #print("Dados validados:", new_cars_form.cleaned_data)  # <-- Verifica os dados limpos antes de salvar
            new_cars_form.save()
            return redirect('cars_list')
        #else:
            print("Erros no formulário:", new_cars_form.errors)  # <-- Verifica se há erros
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