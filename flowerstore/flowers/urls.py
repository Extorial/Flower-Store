from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='flowers.index'),
    path('<int:id>/', views.detail, name='flowers.detail'),
]