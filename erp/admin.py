from django.contrib import admin

from .models import Inventory, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'created_at')
    search_fields = ('name', 'sku')
    list_filter = ('created_at',)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'reorder_level', 'updated_at')
    search_fields = ('product__name', 'product__sku')
