from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    class_count = 0

    if class_count >= settings.DISCOUNT_THRESHOLD:
        discount = total * Decimal(settings.STANDARD_DISCOUNT_PERCENTAGE / 100)
        discount_delta = 0
    else:
        discount = 0
        discount_delta = class_count + 1

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
