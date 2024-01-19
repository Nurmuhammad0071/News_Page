from django.shortcuts import render, get_object_or_404
from .models import New


# Create your views here.
def index(request):
    news = New.object.all()
    context = {
        'news': news
    }
    return render(request, 'biznews/index.html', context)


def show(request, id):
    news = get_object_or_404(New, id=id)
    context = {
        'news': news
    }
    return render(request, 'biznews/show.html', context)


def category(request):
    return render(request, 'biznews/category.html')
