# Generated by Django 3.2.6 on 2021-08-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_shippingaddress_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='riddanceprofile',
            name='address',
            field=models.CharField(default='stz', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='riddanceprofile',
            name='city',
            field=models.CharField(default='stz', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='riddanceprofile',
            name='telephone_number',
            field=models.CharField(default='0888616236', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='riddanceprofile',
            name='zip_code',
            field=models.CharField(default=6000, max_length=4),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]