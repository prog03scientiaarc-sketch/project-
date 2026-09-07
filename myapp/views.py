from django.shortcuts import render
from .models import Item

def home_view(request):
    items = Item.objects.all()
    return render(request, 'myapp/home.html', {'items': items})