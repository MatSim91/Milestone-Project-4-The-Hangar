from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    """ View that retuns cart contents page """
    
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Adding quantity of products to shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list (cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'{product.name} quantity was updated to {cart[item_id]}!')
    else:
        cart[item_id] = quantity
        messages.success(request, f'{product.name} was added to your cart!')
    
    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, item_id):
    """Update the shopping cart product quantity"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'{product.name} quantity was updated to {cart[item_id]}!')
    else:
        cart.pop(item_id)
        messages.success(request, f'{product.name} has been removed from your cart!')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove products from shopping cart"""

    if request.method == "POST":
        try:
            product = get_object_or_404(Product, pk=item_id)
            cart = request.session.get("cart", {})

            cart.pop(item_id)
            messages.success(request, f'{product.name} has been removed from your cart!')

            request.session["cart"] = cart
            return HttpResponse(status=200)

        except Exception as error:
            messages.error(request, f"Error removing item {error}")
            return HttpResponse(status=500)
    else:
        messages.error(request, "Error you do not have permission to do this.")
        return redirect(reverse("home_page"))