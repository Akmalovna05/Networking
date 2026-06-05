from django.urls import path

from . import views

app_name = 'erp'

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('inventory/', views.inventory_list, name='inventory_list'),
]
