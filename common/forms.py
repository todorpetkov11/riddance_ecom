from django import forms

from common.models import Order
from core.forms import BootstrapFormMixin


class OrderForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('receiver', 'product', 'sender')
