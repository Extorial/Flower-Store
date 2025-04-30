from django.shortcuts import render, redirect, get_object_or_404
from .models import Flower, Review
from django.contrib.auth.decorators import login_required

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
    reviews = Review.objects.filter(flower=flower)
    template_data = {'title': flower.name, 'flower': flower, 'reviews': reviews}
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
    
@login_required
def edit_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user != review.user:
        return redirect('flowers.detail', id=id)
    if request.method == 'GET':
        template_data = {'title': 'Edit Review', 'review': review}
        return render(request, 'flowers/edit_review.html', {'template_data': template_data})
    elif request.method == 'POST' and request.POST['comment'] != '':
        review = Review.objects.get(id=review_id)
        review.comment = request.POST['comment']
        review.save()
        return redirect('flowers.detail', id=id)
    else:
        return redirect('flowers.detail', id=id)
    
@login_required
def delete_review(request, id, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    review.delete()
    return redirect('flowers.detail', id=id)
