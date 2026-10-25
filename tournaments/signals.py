from django.db.models.signals import post_delete, pre_save
from django.dispatch.dispatcher import receiver

from .models import Tournament

# Suppression du fichier image d'un tournoi supprimé (Point 3)
@receiver(post_delete, sender=Tournament)
def tournament_post_delete(sender, instance, **kwags):
    if instance.image:
        instance.image.delete(False)

# Suppression de l'ancienne image d'un tournoi, une fois remplacée (Point 3)
@receiver(pre_save, sender=Tournament)
def tournament_pre_save(sender, instance, **kwags):
    if instance.pk:
        try:
            old_image = sender.objects.get(pk=instance.pk).image
            if old_image != instance.image:
                old_image.delete(False)
        except Tournament.DoesNotExist:
            pass