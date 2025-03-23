from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

def register_views(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            redirect('cars_list')
    else:
        user_form = UserCreationForm()

    context = {
        'user_form':user_form
    }

    return render(
        request,
        'register.html',
        context,
    )