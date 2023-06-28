from rest_framework import serializers

from apps.store.models import StoreOrder


class StoreOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreOrder
        fields = ['id', 'order_name', 'order_status']
