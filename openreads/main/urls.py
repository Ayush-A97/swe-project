from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name = 'search'),
]
