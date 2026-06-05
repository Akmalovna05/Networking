from django.contrib import admin

from .models import StockMovement, Warehouse


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'location', 'capacity', 'created_at')
    search_fields = ('name', 'code', 'location')


@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'warehouse', 'movement_type', 'quantity', 'created_at')
    search_fields = ('product__name', 'warehouse__name')
    list_filter = ('movement_type', 'warehouse', 'created_at')
