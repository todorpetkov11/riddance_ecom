from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models
from accounts.managers import RiddanceUserManager


class RiddanceUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True)
    is_staff = models.BooleanField(
        default=False)
    date_joined = models.DateTimeField(
        auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects = RiddanceUserManager()


class RiddanceProfile(models.Model):
    user = models.OneToOneField(
        RiddanceUser, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    profile_image = models.ImageField(
        upload_to='profile', blank=True)
    full_name = models.CharField(
        max_length=50, blank=True)


class ShippingAddress(models.Model):
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=4)
    city = models.CharField(max_length=20)
    user = models.ForeignKey(
        RiddanceUser, on_delete=models.CASCADE, primary_key=True, unique=True, related_name='shipping_address'
    )


from accounts.signals import *
