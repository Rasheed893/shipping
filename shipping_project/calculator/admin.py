from django.contrib import admin

from .models import Device, QuantityRange

# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "base_price")

class QuantityRangeAdmin(admin.ModelAdmin):
    list_display = ("device", "start_qty", "end_qty", "price_per_unit")
    # filter_horizontal = ("flights",)

admin.site.register(Device, DeviceAdmin)
admin.site.register(QuantityRange, QuantityRangeAdmin)
