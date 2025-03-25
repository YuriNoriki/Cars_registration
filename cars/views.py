from django.shortcuts import render,redirect
from cars.models import Car
from cars.forms import  CarModelForm
from django.views import View


class CarsView(View):
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search') 
    
        if search:
            cars = cars.filter(model__icontains = search) 
            
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

class NewCarsView(View):

    def get(self,request):
        new_cars_form = CarModelForm()
        return render(request,'new_cars.html',{'new_cars_form': new_cars_form})
    
    def post(self,request):
        new_cars_form = CarModelForm(request.POST, request.FILES)
        if new_cars_form.is_valid():
            new_cars_form.save()
            return redirect('cars_list')
        return render(request, 'new_cars.html', {'new_cars_form': new_cars_form})