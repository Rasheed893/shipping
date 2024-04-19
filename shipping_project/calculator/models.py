from django.db import models

# Create your models here.


class Device(models.Model):
    name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.base_price})"

class QuantityRange(models.Model):
    device = models.ForeignKey(Device, related_name='quantity_ranges', on_delete=models.CASCADE)
    start_qty = models.IntegerField()
    end_qty = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.start_qty} - {self.end_qty} units: {self.price_per_unit} Euro"

