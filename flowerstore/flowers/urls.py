from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='flowers.index'),
    path('<int:id>/', views.detail, name='flowers.detail'),
    path('<int:id>/review/create/', views.create_review, name='flowers.create_review'),
    path('<int:id>/review/<int:review_id>/edit/', views.edit_review, name='flowers.edit_review'),
    path('<int:id>/review/<int:review_id>/delete/', views.delete_review, name='flowers.delete_review'),
]