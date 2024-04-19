from django.shortcuts import render
from .models import Device, QuantityRange

# Create your views here.


def calculate_shipping(request):
    devices = Device.objects.all()
    total_price = None  # Initialize total_price as None

    if request.method == 'POST':
        device_id = request.POST.get('device')
        quantity = int(request.POST.get('quantity'))
        device = Device.objects.get(pk=device_id)
        quantity_range = device.quantity_ranges.filter(start_qty__lte=quantity, end_qty__gte=quantity).first()
        if quantity_range:
            total_price = quantity * quantity_range.price_per_unit

    context = {
        'devices': devices,
        'total_price': total_price
    }
    return render(request, 'calculator/calculate.html', context)
