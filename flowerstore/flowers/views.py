from django.shortcuts import render, redirect
from .models import Flower, Review
from django.contrib.auth.models import login_required

# Create your views here.
flowers = [
    
]

def index(request):
    search_term = request.GET.get('search')
    if (search_term):
        flowers = Flower.objects.filter(name__icontains=search_term)
    else:
        flowers = Flower.objects.all()
    template_data = {'title': 'Flowers', 'flowers': flowers}
    return render(request, 'flowers/index.html', {'template_data' : template_data})

def detail(request, id):
    flower = Flower.objects.get(id=id)
    template_data = {'title': flower.name, 'flower': flower}
    return render(request, 'flowers/detail.html', {'template_data' : template_data})

@login_required
def create_review(request, id):
    if request.method == 'POST' and request.POST['comment'] != '':
        flower = Flower.objects.get(id=id)
        review = Review()
        review.comment = request.POST['comment']
        review.flower = flower
        review.user = request.user
        review.save()
        return redirect('flowers.detail', id=id)
    else:
        return redirect('flowers.detail', id=id)
