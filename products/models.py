from PIL import Image
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

from products.validators import image_validator

UserModel = get_user_model()


class ProductModel(models.Model):
    CATEGORY_CHOICES = (
        ('Shorts', 'Shorts'),
        ('T-Shirts', 'T-Shirts'),
        ('Shirts', 'Shirts'),
        ('Blouses', 'Blouses'),
        ('Pants', 'Pants'),
        ('Shoes', 'Shoes'),
        ('Boots', 'Boots'),
        ('Flip-flops', 'Flip-flops'),
        ('Tops', 'Tops'),
    )
    name = models.CharField(
        max_length=50)
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(
        auto_now_add=True)
    description = models.TextField(
        max_length=300
    )
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        max_length=15
    )
    price = models.DecimalField(
        max_digits=6, decimal_places=2)

    thumbnail = models.FileField(
        upload_to='products/thumbnails/', validators=[image_validator]
    )

    def save(self, *args, **kwargs):
        super(ProductModel, self).save()
        img = Image.open(self.thumbnail.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.thumbnail.path)


"""
        def save(self) overrides the thumbanail save, resizing it
        to the proper dimensions.
"""


class ImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to='products/', validators=[image_validator])
    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, null=True)