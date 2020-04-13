from django.contrib import admin
from .models import *

class LibraryAdmin(admin.ModelAdmin):
    list_display = ['id']
    pass
admin.site.register(Library, LibraryAdmin)

class ShelfAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    pass

admin.site.register(Shelf, ShelfAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    pass

admin.site.register(Book, BookAdmin)
