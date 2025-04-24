from django.contrib import admin
from .models import Flower
# Register your models here.

class FlowerAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Flower, FlowerAdmin)

