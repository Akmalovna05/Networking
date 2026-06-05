from django.contrib import admin

from .models import Customer, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'email', 'phone', 'created_at')
    search_fields = ('name', 'company', 'email')
    list_filter = ('created_at',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('reference', 'customer', 'total_amount', 'status', 'created_at')
    search_fields = ('reference', 'customer__name')
    list_filter = ('status', 'created_at')
