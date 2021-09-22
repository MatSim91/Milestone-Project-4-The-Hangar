from django.contrib import admin
from .models import Product, Category, Manufacturer, Type

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'type',
        'manufacturer',
        'name',
        'description',
        'price',
        'image',
    )

    ordering = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
    )

class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'thrust',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Type, TypeAdmin)