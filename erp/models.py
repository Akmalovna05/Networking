from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.sku})'

    def get_absolute_url(self):
        return reverse('erp:product_list')


class Inventory(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name='inventory'
    )
    quantity = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['product__name']
        verbose_name_plural = 'Inventories'

    def __str__(self):
        return f'{self.product.name}: {self.quantity}'

    @property
    def needs_reorder(self):
        return self.quantity <= self.reorder_level
