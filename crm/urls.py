from django.urls import path

from . import views

app_name = 'crm'

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('orders/', views.order_list, name='order_list'),
]
