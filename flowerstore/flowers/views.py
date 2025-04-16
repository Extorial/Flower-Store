from django.shortcuts import render

# Create your views here.
flowers = [
    {
        'id': 1, 'name': 'Rose', 'price': 14.99, 'description': 'A beautiful red rose.'
    },
    {
        'id': 2, 'name': 'Dandelion', 'price': 10.99, 'description': 'A petite dandelion.'
    },
    {
        'id': 3, 'name': 'Tulip', 'price': 13.99, 'description': 'A gorgeous orange tulip.'
    },
    {
        'id': 4, 'name': 'Sakura', 'price': 21.99, 'description': 'A smattering of pink sakura blossoms.'
    },
]

def index(request):
    template_data = {'title': 'Flowers', 'flowers': flowers}
    return render(request, 'flowers/index.html', {'template_data' : template_data})

def detail(request, id):
    flower = flowers[id - 1]
    template_data = {'title': flower['name'], 'flower': flower}
    return render(request, 'flowers/detail.html', {'template_data' : template_data})