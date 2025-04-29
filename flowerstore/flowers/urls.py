from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='flowers.index'),
    path('<int:id>/', views.detail, name='flowers.detail'),
    path('<int:id>/review/create/', views.create_review, name='flowers.create_review'),
]