from django.shortcuts import render
from .models import New


# Create your views here.
def index(request):
    news = New.object.all()
    context = {
        'news': news
    }
    return render(request, 'biznews/index.html', context)


def category(request):
    return render(request, 'biznews/category.html')
