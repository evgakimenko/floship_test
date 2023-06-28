from django.contrib import admin

from apps.store.models import StoreOrder


class StoreAdminSite(admin.AdminSite):
    site_header = 'Store Admin'
    site_title = 'Store Admin Portal'
    index_title = 'Welcome to Store Admin Portal'


class ModelSettings(admin.ModelAdmin):
    list_display = ['id', 'order_name']


store_admin_site = StoreAdminSite(name='store_admin')

store_admin_site.register(StoreOrder, ModelSettings)
