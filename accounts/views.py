from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register_views(request):
    user_form = UserCreationForm()

    context = {
        'user_form':user_form
    }

    return render(
        request,
        'register.html',
        context,
    )