import uuid

from django.db import models


class StoreOrder(models.Model):
    status_choices = (
        (1, "Open"),
        (1, "In Progress"),
        (2, "Closed"),
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    order_name = models.CharField(max_length=255, blank=False)
    order_status = models.IntegerField(max_length=255, blank=False, choices=status_choices)
