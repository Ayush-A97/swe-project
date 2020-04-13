from django.shortcuts import render
from .models import *
from user.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        currUser = User.objects.get(username = request.user.username)
        libId = currUser.lib
        print(libId)
        shelves = libId.shelf_set.all()
        print(shelves)

        for shelf in shelves:
            print(shelf.book_set.all())
        return render(request, 'main/home.html', {'shelves': shelves})

    else:
        return render(request, 'main/home.html')

def search(request):
    keyword = request.GET['searchword']
    # data = book_search(keyword, None)
    # res = {}
    # res['items'] = data
    return render(request, 'main/search.html', {'data': res})