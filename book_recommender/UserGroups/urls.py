from django.urls import path, re_path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('create/', views.create, name = 'createGroup'),
    path('join/<int:id>/', views.join_group, name = 'join_group'),
    url(r'(?P<id>[0-9]+)/$', views.details, name = "groupDetails"),
    url(r'(?P<bid>[0-9]+)/(?P<gid>[0-9]+)$', views.addBookToGroup, name = "addBookToGroup"),

    # path('logout/', LogoutView.as_view(next_page='/')),
    # path('register/', views.register, name="register"),
    # path('account/', views.view_profile, name = "view_profile"),
    # path('account/edit',views.edit_profile, name = "edit_profile")
]
