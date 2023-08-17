from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from jobapp.models import Circular, savedCircular


@receiver(post_save, sender=Circular)
def onCircularUpdated(sender, instance, **kwargs):
    print("post saved")


@receiver(post_delete, sender=savedCircular)
def onCircularUpdated(sender, instance, **kwargs):
    print("post deleted")


@receiver(post_save, sender=savedCircular)
def onCircularUpdated(sender, instance, **kwargs):
    print("post saved")
