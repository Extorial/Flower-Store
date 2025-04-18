from django.shortcuts import render
from .models import Flower

# Create your views here.
flowers = [
    
]

def index(request):
    template_data = {'title': 'Flowers', 'flowers': Flower.objects.all()}
    return render(request, 'flowers/index.html', {'template_data' : template_data})

def detail(request, id):
    flower = flowers[id - 1]
    template_data = {'title': flower['name'], 'flower': flower}
    return render(request, 'flowers/detail.html', {'template_data' : template_data})