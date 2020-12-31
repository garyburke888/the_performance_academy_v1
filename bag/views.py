from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from classes.models import Class

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    a_class = get_object_or_404(Class, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    day = None
    if 'class_day' in request.POST:
        day = request.POST['class_day']
    bag = request.session.get('bag', {})

    if day:
        if item_id in list(bag.keys()):
            if day in bag[item_id]['items_by_day'].keys():
                bag[item_id]['items_by_day'][day] += quantity
                messages.success(request, f'Updated day {day.upper()} {a_class.name} quantity to {bag[item_id]["items_by_day"][day]}')
            else:
                bag[item_id]['items_by_day'][day] = quantity
                messages.success(request, f'Added day {day.upper()} {a_class.name} to your bag')
        else:
            bag[item_id] = {'items_by_day': {day: quantity}}
            messages.success(request, f'Added day {day.upper()} {a_class.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {a_class.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {a_class.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    a_class = get_object_or_404(Class, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    day = None
    if 'class_day' in request.POST:
        day = request.POST['class_day']
    bag = request.session.get('bag', {})

    if day:
        if quantity > 0:
            bag[item_id]['items_by_day'][day] = quantity
            messages.success(request, f'Updated day {day.upper()} {a_class.name} quantity to {bag[item_id]["items_by_day"][day]}')
        else:
            del bag[item_id]['items_by_day'][day]
            if not bag[item_id]['items_by_day']:
                bag.pop(item_id)
            messages.success(request, f'Removed day {day.upper()} {a_class.name} from your bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {a_class.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {a_class.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        a_class = get_object_or_404(Class, pk=item_id)
        day = None
        if 'class_day' in request.POST:
            day = request.POST['class_day']
        bag = request.session.get('bag', {})

        if day:
            del bag[item_id]['items_by_day'][day]
            if not bag[item_id]['items_by_day']:
                bag.pop(item_id)
            messages.success(request, f'Removed day {day.upper()} {a_class.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {a_class.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
