from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from classes.models import Class


def bag_contents(request):

    bag_items = []
    total = 0
    class_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            a_class = get_object_or_404(Class, pk=item_id)
            total += item_data * a_class.price
            class_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'class': a_class,
            })
        else:
            a_class = get_object_or_404(Class, pk=item_id)
            for day, quantity in item_data['items_by_day'].items():
                total += quantity * a_class.price
                class_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'class': a_class,
                    'day': day,
                })

    if class_count >= settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE / 100)
        discount_delta = 0
    else:
        discount = 0
        discount_delta = 2 - class_count

    grand_total = total - discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'class_count': class_count,
        'discount': discount,
        'discount_delta': discount_delta,
        'discount_threshold': settings.DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

