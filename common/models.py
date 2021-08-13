from django.db import models

from accounts.models import RiddanceUser
from common.validators import phone_validator, full_name_validator, zip_code_validator
from products.models import ProductModel


class Order(models.Model):
    SHIPPING_CHOICE = (
        ('econt', 'Econt'),
        ('speedy', 'Speedy')
    )
    sender = models.ForeignKey(RiddanceUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(RiddanceUser, on_delete=models.CASCADE, related_name='receiver')
    full_name = models.CharField(
        max_length=50, blank=True, validators=[full_name_validator])
    telephone_number = models.CharField(max_length=10, validators=[phone_validator])
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=4, validators=[zip_code_validator])
    shipping_method = models.CharField(max_length=10, choices=SHIPPING_CHOICE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

