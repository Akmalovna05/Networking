from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Customer, Order


@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customer_list.html', {'customers': customers})


@login_required
def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'crm/customer_detail.html', {'customer': customer})


@login_required
def order_list(request):
    orders = Order.objects.select_related('customer').all()
    return render(request, 'crm/order_list.html', {'orders': orders})
