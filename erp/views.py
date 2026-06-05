from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Inventory, Product


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'erp/product_list.html', {'products': products})


@login_required
def inventory_list(request):
    inventory = Inventory.objects.select_related('product').all()
    return render(request, 'erp/inventory_list.html', {'inventory': inventory})
