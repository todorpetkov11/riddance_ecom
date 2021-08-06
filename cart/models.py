from django.db import models

from accounts.models import RiddanceUser
from products.models import ProductModel


class CartProduct(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.OneToOneField(RiddanceUser, on_delete=models.CASCADE, primary_key=True, related_name='cart')
    items = models.ManyToManyField(CartProduct)
    ordered = models.BooleanField(default=False)

    def count_items(self):
        count = self.items.count()
        return count

    def get_total_price(self):
        total = 0
        for item in self.items.all():
            total += item.product.price
        return total
