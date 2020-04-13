from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UserForm, User
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate

# Create your views here.

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()
    return render(request, 'user/register.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
         pass
    else:
        return LoginView.as_view(template_name='user/login.html')(request)

def logout(request):
    if request.user.is_authenticated:
        LogoutView.as_view(template_name='main/home.html')(request)
    return HttpResponseRedirect('/')

def view_profile(request, user_id):
    
    return render(request, 'user/profile.html', {})