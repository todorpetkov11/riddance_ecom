from django import forms

from core.forms import BootstrapFormMixin
from products.models import ProductModel, ImageModel


class ProductForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = ProductModel
        exclude = ('user',)


class ImageForm( BootstrapFormMixin, forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = ImageModel
        fields = ('image',)


