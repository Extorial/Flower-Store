from django.contrib import admin
from .models import Flower, Review
# Register your models here.

class FlowerAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Flower, FlowerAdmin)
admin.site.register(Review)

