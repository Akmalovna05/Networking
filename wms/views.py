from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import StockMovement, Warehouse


@login_required
def warehouse_list(request):
    warehouses = Warehouse.objects.all()
    return render(request, 'wms/warehouse_list.html', {'warehouses': warehouses})


@login_required
def stock_movement_list(request):
    movements = StockMovement.objects.select_related('product', 'warehouse').all()
    return render(request, 'wms/stock_movement_list.html', {'movements': movements})
