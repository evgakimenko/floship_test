import json

from django.contrib import admin

from apps.warehouse.components.request import SendRequest
from apps.warehouse.models import WarehouseOrder


class WarehouseAdminSite(admin.AdminSite):
    site_header = 'Warehouse Admin'
    site_title = 'Warehouse Admin Portal'
    index_title = 'Welcome to Warehouse Admin Portal'


class ModelSettings(admin.ModelAdmin):
    list_display = ['id', 'order_name']

    def has_add_permission(self, request):
        return False

    # Comment this code if only create order is required in warehouse from store
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        data = {
            'id': str(obj.id),
            'order_name': obj.order_name,
            'order_status': obj.order_status,
        }
        if change:
            post_data = json.dumps(data)
            SendRequest().put_order(post_data)


warehouse_admin_site = WarehouseAdminSite(name='warehouse_admin')

warehouse_admin_site.register(WarehouseOrder, ModelSettings)
