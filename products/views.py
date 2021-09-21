from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Type

# Create your views here.

def all_products(request):
    """ View that returns all products, and also include sorting and search """

    products = Product.objects.all()
    query = None
    types = None

    if request.GET:
        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            products = products.filter(type__name__in=types)
            types = Type.objects.filter(name__in=types)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please type a search criteria.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_types': types,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ View that returns the details of the specific product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)