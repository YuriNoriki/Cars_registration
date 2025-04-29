from django.db.models.signals import pre_save,pre_delete,post_delete,post_save
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car,CarIventory

def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']

    CarIventory.objects.create(
        car_count = cars_count,
        car_value = cars_value
    )

@receiver(post_save,sender = Car)
def car_post_save(sender,instance, **kwargs):
    car_inventory_update()
    

@receiver(post_delete,sender = Car)
def car_pre_save(sender,instance, **kwargs):
   car_inventory_update()
