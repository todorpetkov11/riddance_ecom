from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class ProductModel(models.Model):
    CATEGORY_CHOICES = (
        ('shorts', 'Shorts'),
        ('tshirt', 'T-Shirts'),
        ('blouses', 'Blouses'),
        ('pants', 'Pants'),
        ('boots', 'boots'),
        ('flipflops', 'Flip-flops'),
        ('tops', 'Tops'),
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
        upload_to='products/thumbnails/'
    )

    def save(self):
        super(ProductModel, self).save()
        img = Image.open(self.thumbnail.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.thumbnail.path)


class ImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to='products/')
    default = models.BooleanField(default=False)
