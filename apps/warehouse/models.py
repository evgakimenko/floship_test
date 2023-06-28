import environ

from django.db import models


class WarehouseOrder(models.Model):
    status_choices = (
        (0, "Open"),
        (1, "In Progress"),
        (2, "Closed"),
    )

    id = models.UUIDField(primary_key=True, editable=False)
    order_name = models.CharField(max_length=255, blank=False)
    order_status = models.IntegerField(max_length=255, blank=False, choices=status_choices)
