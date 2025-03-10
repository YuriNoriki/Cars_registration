from django.shortcuts import render
from django.http import HttpResponse

def cars_views(request):
    return HttpResponse('Meu carro')
