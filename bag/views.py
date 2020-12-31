from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

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

    request.session['bag'] = bag
    return redirect(redirect_url)
