from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from crm.models import Customer, Order
from erp.models import Product
from wms.models import Warehouse


@login_required
def home(request):
    context = {
        'customer_count': Customer.objects.count(),
        'order_count': Order.objects.count(),
        'product_count': Product.objects.count(),
        'warehouse_count': Warehouse.objects.count(),
    }
    return render(request, 'dashboard/home.html', context)
