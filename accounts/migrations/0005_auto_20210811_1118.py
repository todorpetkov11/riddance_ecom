# Generated by Django 3.2.6 on 2021-08-11 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210811_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='riddanceprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='riddanceprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='riddanceprofile',
            name='zip_code',
        ),
    ]