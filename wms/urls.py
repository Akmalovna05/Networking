from django.urls import path

from . import views

app_name = 'wms'

urlpatterns = [
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('movements/', views.stock_movement_list, name='stock_movement_list'),
]
