from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'biznews/index.html')


def category(request):
    return render(request, 'biznews/category.html')
