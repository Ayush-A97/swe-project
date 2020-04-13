from django.db import models

# Create your models here.
class Library(models.Model):
    #
    pass

class Shelf(models.Model):
    lib = models.ForeignKey(Library, on_delete=models.CASCADE, null=True)
    pass

class Book(models.Model):
    # id
    # Other stuff like genre, etc.
    # rating
    shelves = models.ManyToManyField(Shelf)
    pass

class Rating(models.Model):
    ## UserId
    ## BookID
    ## Rating
    ## Maybe shelf id?
    pass