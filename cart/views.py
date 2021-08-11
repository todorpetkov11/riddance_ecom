from django.contrib import messages
from django.shortcuts import render, redirect

from cart.models import Cart, CartProduct
from products.models import ProductModel


def get_cart(request):
    try:
        cart = Cart.objects.get(user=request.user, ordered=False)
    except:
        cart = Cart.objects.create(user=request.user, ordered=False)
        cart.save()

    return cart


"""
        Gets the current user's cart or of it doesn't exist
        it creates a new one saves it to the database.
"""


def add_to_cart(request, pk):
    product = ProductModel.objects.get(pk=pk)
    item, created = CartProduct.objects.get_or_create(product=product)
    cart = get_cart(request)
    if cart.items.filter(cart__items__product_id=product.pk).exists():
        messages.info(request, "This item is already in your cart")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        cart.items.add(item)
        messages.info(request, "Item added to cart")
        return redirect(request.META.get('HTTP_REFERER'))


"""
        Converts a product object into a cart product object and
        checks and checks if it is already in the current user's 
        cart.
        Displays a massage and redirects to the previous page
        afterwards.
"""


def remove_from_cart(request, pk):
    product = ProductModel.objects.get(pk=pk)
    item, created = CartProduct.objects.get_or_create(product=product)
    cart = get_cart(request)
    if cart.items.filter(cart__items__product_id=product.pk).exists():
        cart.items.remove(item)
        item.delete()
        if cart.items.count() == 0:
            cart.delete()
        messages.info(request, "Item removed from cart")
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.info(request, "Item not in cart yet")
        return redirect(request.META.get('HTTP_REFERER'))


"""
        Gets or creates a cart product object and
        checks and checks if it is already in the current user's 
        cart.
        Displays a massage and redirects to the previous page
        afterwards.
        If the cart is emptied by removing the item from the
        items' table, it deletes both the CartProduct and the Cart.
"""


def cart_details(request):
    cart = get_cart(request)
    items = cart.items.all()
    context = {
        'items': items,
        'cart': cart,
    }
    return render(request, 'cart/cart_details.html', context)


"""
        Displays the cart and the items that are currently in it.
"""
