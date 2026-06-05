from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=255, blank=True)
    capacity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.code})'


class StockMovement(models.Model):
    MOVEMENT_CHOICES = [
        ('in', 'Inbound'),
        ('out', 'Outbound'),
        ('transfer', 'Transfer'),
    ]

    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, related_name='movements'
    )
    product = models.ForeignKey(
        'erp.Product', on_delete=models.CASCADE, related_name='stock_movements'
    )
    movement_type = models.CharField(max_length=20, choices=MOVEMENT_CHOICES)
    quantity = models.IntegerField(default=0)
    note = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_movement_type_display()} - {self.product} ({self.quantity})'
