from django.urls import path
from news.views import *

urlpatterns = [
    path('', index, name='home'),
    path('category', index, name='category'),
    path('show/<int:id>', show, name='show'),
]
