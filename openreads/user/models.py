from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser

from main.models import Library
from group.models import Group

class User(AbstractUser):
    lib = models.OneToOneField(Library, on_delete = models.CASCADE, null=True)
    groups = models.ManyToManyField(Group, blank=True)

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=120)

    class Meta:
        model = User
        fields = ['username', 'password']
        labesl = {
            'username': "Username",
            'password': "Password",
            'confirm_pasword': "Confirm Password",
        }
        def clean(self):
            cleaned_data = super(UserForm, self).clean()
            passw = cleaned_data.get('password')
            c_passw = cleaned_data.get('confirm_password')

            if passw and c_passw and passw != c_passw:
                    raise forms.ValidationError("Passwords do not match!")