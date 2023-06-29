import json

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.warehouse.components.request import SendRequest


class WarehouseOrder(models.Model):
    status_choices = (
        (0, "Open"),
        (1, "In Progress"),
        (2, "Closed"),
    )

    id = models.UUIDField(primary_key=True)
    order_name = models.CharField(max_length=255, blank=False)
    order_status = models.IntegerField(blank=False, choices=status_choices)

    class Meta:
        app_label = 'warehouse'

    # Uncomment this code if only create order is required in warehouse from store
# @receiver(post_save, sender=WarehouseOrder)
# def send_order_update(instance, created, **kwargs):
#     if not created:
#         data = {
#             'id': str(instance.id),
#             'order_name': instance.order_name,
#             'order_status': instance.order_status,
#         }
#         post_data = json.dumps(data)
#         SendRequest().put_order(post_data)
