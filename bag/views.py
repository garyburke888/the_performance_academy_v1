from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from classes.models import Class

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    a_class = Class.objects.get(pk=item_id)
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
            else:
                bag[item_id]['items_by_day'][day] = quantity
        else:
            bag[item_id] = {'items_by_day': {day: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {a_class.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    day = None
    if 'class_day' in request.POST:
        day = request.POST['class_day']
    bag = request.session.get('bag', {})

    if day:
        if quantity > 0:
            bag[item_id]['items_by_day'][day] = quantity
        else:
            del bag[item_id]['items_by_day'][day]
            if not bag[item_id]['items_by_day']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        day = None
        if 'class_day' in request.POST:
            day = request.POST['class_day']
        bag = request.session.get('bag', {})

        if day:
            del bag[item_id]['items_by_day'][day]
            if not bag[item_id]['items_by_day']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
