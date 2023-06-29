import json

from django.contrib import admin

from apps.store.components.request import SendRequest
from apps.store.models import StoreOrder


class StoreAdminSite(admin.AdminSite):
    site_header = 'Store Admin'
    site_title = 'Store Admin Portal'
    index_title = 'Welcome to Store Admin Portal'


class ModelSettings(admin.ModelAdmin):
    list_display = ['id', 'order_name']

    # Comment this code if only create order is required in warehouse from store
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        data = {
            'id': str(obj.id),
            'order_name': obj.order_name,
            'order_status': obj.order_status,
        }
        json_data = json.dumps(data)
        if not change:
            SendRequest().post_order(json_data)
        else:
            SendRequest().put_order(json_data)


store_admin_site = StoreAdminSite(name='store_admin')

store_admin_site.register(StoreOrder, ModelSettings)
