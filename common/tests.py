from django.db.models import QuerySet
from django.test import TestCase, Client
from accounts.models import RiddanceUser
from cart.models import Cart
from common.forms import OrderForm
from common.models import Order
from products.models import ProductModel


class TestViews(TestCase):

    def setUp(self):
        self.test_client = Client()
        self.test_client = Client()
        self.user = RiddanceUser.objects.create_user("example@example.com", '123123')
        self.user_two = RiddanceUser.objects.create_user("example@abv.com", '123123')
        self.product = ProductModel(name='Product', category='Pants', user=self.user_two, price=123,
                                    thumbnail='riddance.png',
                                    description='asdasd')
        self.test_client.login(email='example@example.com', password='123123')
        self.order = Order(full_name='Todor Todor', shipping_method='speedy', address='asd',
                           telephone_number='0888123123', city='stara zagora', zip_code='6000',
                           receiver=self.user_two, sender=self.user, product=self.product)

    def test_if_browse_view_returns_template_and_context(self):
        response = self.test_client.get('/')
        self.assertTemplateUsed(response, 'browsing/index.html')
        self.assertIsInstance(response.context['object_list'], QuerySet)

    def test_checkout_return_template_and_context(self):
        response = self.test_client.get('/checkout/')
        self.assertTemplateUsed(response, 'orders_and_checkout/checkout.html')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['cart'], Cart)
        self.assertIsInstance(response.context['form'], OrderForm)

