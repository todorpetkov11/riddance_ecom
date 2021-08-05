from django.urls import path

from cart.views import add_to_cart, remove_from_cart, cart_details

urlpatterns = [
    path('add_to_cart/<int:pk>', add_to_cart, name='add to cart'),
    path('remove_from_cart/<int:pk>', remove_from_cart, name='remove from cart'),
    path('cart_details/', cart_details, name='cart details')
]
