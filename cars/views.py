from cars.models import Car
from cars.forms import  CarModelForm
from django.views.generic import ListView, CreateView


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