from django.contrib import admin

# Register your models here.
from .models import Category, Items

admin.site.register(Category)# agrego el item categorias a djando administration
admin.site.register(Items)