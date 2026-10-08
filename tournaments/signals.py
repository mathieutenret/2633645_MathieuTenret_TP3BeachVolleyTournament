from django.db.models.signals import post_delete, pre_save
from django.dispatch.dispatcher import receiver

from .models import Tournament

@receiver(post_delete, sender=Tournament)
def product_post_delete(sender, instance, **kwags):
    instance.image.delete(False)

@receiver(pre_save, sender=Tournament)
def product_pre_save(sender, instance, **kwags):
    if instance.pk:
        try:
            old_image = sender.objects.get(pk=instance.pk).image
            if old_image != instance.image:
                old_image.delete(False)
        except Tournament.DoesNotExist:
            pass