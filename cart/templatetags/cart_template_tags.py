from django import template
from cart.models import Cart

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        cart = Cart.objects.filter(user=user, ordered=False)
        if cart.exists():
            return cart[0].count_items()
    return 0


"""
        Provides the number of items in the cart to the template.
"""
