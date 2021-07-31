from django import forms

from products.models import ProductModel, ImageModel


class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        exclude = ('user',)


class ImageForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = ImageModel
        fields = ('image',)

