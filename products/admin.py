from django.contrib import admin
from .models import Product, Category, Manufacturer, Type

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Type)