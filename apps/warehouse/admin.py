from django.contrib import admin

from apps.warehouse.models import WarehouseOrder


class WarehouseAdminSite(admin.AdminSite):
    site_header = 'Warehouse Admin'
    site_title = 'Warehouse Admin Portal'
    index_title = 'Welcome to Warehouse Admin Portal'


class ModelSettings(admin.ModelAdmin):
    list_display = ['id', 'order_name']


warehouse_admin_site = WarehouseAdminSite(name='warehouse_admin')

warehouse_admin_site.register(WarehouseOrder, ModelSettings)
