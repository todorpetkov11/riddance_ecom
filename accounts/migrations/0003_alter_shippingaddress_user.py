# Generated by Django 3.2.6 on 2021-08-04 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_shippingaddress_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='shipping_address', serialize=False, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
