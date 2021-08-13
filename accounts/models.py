from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models
from accounts.managers import RiddanceUserManager
from accounts.validators import phone_validator, full_name_validator


class RiddanceUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True, max_length=50)
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
        max_length=50, blank=True, validators=[full_name_validator])
    telephone_number = models.CharField(max_length=10, validators=[phone_validator])



from accounts.signals import *
