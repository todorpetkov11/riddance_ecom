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


def cart_details(request):
    cart = get_cart(request)
    items = cart.items.all()
    context = {
        'items': items,
        'cart': cart,
    }
    return render(request, 'cart_details.html', context)
