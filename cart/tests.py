from django.test import TestCase

from accounts.models import RiddanceUser
from cart.models import Cart, CartProduct
from products.models import ProductModel


class TestCart(TestCase):

    def setUp(self):
        self.user = RiddanceUser.objects.create_user('example@example.com', '123123')
        self.user_two = RiddanceUser.objects.create_user('two@two.com', '123123')
        self.user_three = RiddanceUser.objects.create_user('three@three.com', '123123')
        self.product = ProductModel.objects.create(name='asd', price=123, category='Boots', user=self.user_two,
                                                   thumbnail='riddance.png', description='asd')
        self.cart_product_one = CartProduct(product=self.product)
        self.cart = Cart(user=self.user)
        self.cart.items.add(self.cart_product_one)

    def test_cart_count_items(self):
        count = self.cart.count_items()
        self.assertEqual(count, 2)
