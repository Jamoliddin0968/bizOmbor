from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.versions.models import Version

from .models import Product


@receiver(pre_save, sender=Product)
def set_version(sender, instance, **kwargs):
    if not instance.version:
        instance.version = Version.objects.create()
