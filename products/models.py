from django.db import models

# Create your models here.

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    manufacturer = models.ForeignKey('Manufacturer', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Manufacturer(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    country = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    thrust = models.CharField(max_length=30)

    def __str__(self):
        return self.name