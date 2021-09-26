from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Je361IvND6rEWdIJ9EaqSzcbcrZWfkDd8GgMNbptpUMpaaNPFluIlg5t533bNy6M8q47cFnuVKCJTvlOzBvaizB00fyS8qIi5',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)