"""
URL configuration for floship_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from apps.store.admin import store_admin_site
from apps.store.views import StoreOrderView
from apps.warehouse.admin import warehouse_admin_site
from apps.warehouse.views import WarehouseOrderView

urlpatterns = [
    path('warehouse/admin/', warehouse_admin_site.urls),
    path('store/admin/', store_admin_site.urls),
    path('warehouse/api/create/order/', WarehouseOrderView.as_view(), name='warehouse_order_create_api_view', ),
    path('store/api/update/order/', StoreOrderView.as_view(), name='store_order_update_api_view', ),
    path('warehouse/api/update/order/', WarehouseOrderView.as_view(), name='warehouse_order_update_api_view', ),
]
