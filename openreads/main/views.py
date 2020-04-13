from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def search(request):
    keyword = request.GET['searchword']
    # data = book_search(keyword, None)
    # res = {}
    # res['items'] = data
    return render(request, 'main/search.html', {'data': res})