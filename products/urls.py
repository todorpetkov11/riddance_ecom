from django.urls import path
from products.views import add_product, edit_product, delete_product, product_details

urlpatterns = [
    path('add/', add_product, name='add product'),
    path('edit/<int:pk>', edit_product, name='edit product'),
    path('delete/<int:pk>', delete_product, name='delete product'),
    path('details/<int:pk>', product_details, name='product details')
]
