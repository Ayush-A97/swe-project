from django.shortcuts import render
from django.shortcuts import render,redirect
from Books.models import *
from django.views.generic import View
from django.contrib.auth.views import LoginView

def index(request):
    return render(request,'login.html', {})

