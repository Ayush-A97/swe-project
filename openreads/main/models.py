from django.db import models

# Create your models here.
class Library(models.Model):
    pass

class Shelf(models.Model):
    name = models.CharField(max_length=256, default='shelf')
    lib = models.ForeignKey(Library, on_delete=models.CASCADE, null=True)
    pass

class Book(models.Model):
    title = models.CharField(max_length = 512)
    author = models.CharField(max_length = 256)
    year_pub = models.CharField(max_length = 4)
    cover = models.CharField(max_length = 512)
    description = models.TextField(max_length = 1024)
    rating = models.IntegerField(default = 0)
    shelves = models.ManyToManyField(Shelf, blank=True)

class Rating(models.Model):
    ## UserId
    ## BookID
    ## Rating
    ## Maybe shelf id?
    pass