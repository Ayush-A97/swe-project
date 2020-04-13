from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('profile/<user_id>/', views.view_profile, name = 'view_profile'),
    # path('student/profile', views.profile_student, name='profile_student'),
]