from django.shortcuts import render

# Create your views here.
def index(request):
    template_data = {} #to pass data from views to template
    template_data['title'] = 'Flower Store'
    return render(request, 'home/index.html', {
        'template_data': template_data
    })
def about(request):
    template_data = {} #to pass data from views to template
    template_data['title'] = 'Flower Store'
    return render(request, 'home/about.html', {
        'template_data': template_data
    })   
