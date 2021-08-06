from django.contrib import admin
from products.models import ProductModel, ImageModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'category', 'date_added')
    list_filter = ('name', 'user', 'category')


@admin.register(ImageModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'user',)
