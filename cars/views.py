from cars.models import Car
from cars.forms import  CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


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


class NewCreateCar(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_cars.html'
    success_url = 'cars/'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    
class carUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'