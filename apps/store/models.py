import json
import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.store.components.request import SendRequest


class StoreOrder(models.Model):
    status_choices = (
        (0, "Open"),
        (1, "In Progress"),
        (2, "Closed"),
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    order_name = models.CharField(max_length=255, blank=False)
    order_status = models.IntegerField(blank=False, choices=status_choices)

    class Meta:
        app_label = 'store'


@receiver(post_save, sender=StoreOrder)
def send_email_otp(instance, created, **kwargs):
    if created:
        data = {
            'id': str(instance.id),
            'order_name': instance.order_name,
            'order_status': instance.order_status,
        }
        post_data = json.dumps(data)
        SendRequest().post_order(post_data)
