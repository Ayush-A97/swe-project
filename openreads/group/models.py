from django.db import models
from main.models import Library
# Create your models here.

class Group(models.Model):
    lib = models.OneToOneField(Library, on_delete = models.CASCADE, null=True)
    
    pass

class Post(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    pass
