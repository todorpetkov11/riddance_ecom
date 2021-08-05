from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import RiddanceProfile, ShippingAddress

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = RiddanceProfile(
            user=instance)
        profile.save()
        shipping_address = ShippingAddress(
            user=instance
        )
        shipping_address.save()


