from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from flowers.models import Flower
from .utils import calculate_cart_total

# Create your views here.
def index(request):
    cart_total = 0
    flowers_in_cart = []
    cart = request.session.get('cart', {})
    flower_ids = list(cart.keys())
    if (flower_ids != []):
        flowers_in_cart = Flower.objects.filter(id__in=flower_ids)
        cart_total = calculate_cart_total(cart, flowers_in_cart)
    template_data = {'title': 'Cart', 'flowers_in_cart': flowers_in_cart, 'cart_total': cart_total}
    return render(request, 'cart/index.html', {'template_data': template_data})

def add(request, id):
    get_object_or_404(Flower, id=id)
    cart = request.session.get('cart', {})
    cart[id] = request.POST['quantity']
    request.session['cart'] = cart
    return redirect('cart.index')

def clear(request):
    request.session['cart'] = {}
    return redirect('cart.index')


