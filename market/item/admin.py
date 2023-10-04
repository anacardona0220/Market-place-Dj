from django.contrib import admin

# Register your models here.
from .models import Category, Item

admin.site.register(Category)# agrego el item categorias a djando administration
admin.site.register(Item)