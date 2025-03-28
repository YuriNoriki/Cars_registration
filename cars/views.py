from django.shortcuts import render,redirect
from cars.models import Car
from cars.forms import  CarModelForm
from django.views import View
from django.views.generic import ListView


class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        # Chama o método get_queryset() da classe ListView e retorna os objetos do modelo Car
        cars = super().get_queryset().order_by('model')
        
         # Verifica se há um parâmetro de busca na URL (exemplo: ?search=Toyota)
        search = self.request.GET.get('search')
        
         # Filtra os carros com base no termo de pesquisa (ignorando maiúsculas/minúsculas)
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

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