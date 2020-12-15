from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Class

# Create your views here.


def all_classes(request):
    """ A view to show all classes, including sorting and search queries """

    classes = Class.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('classes'))
                
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            classes = classes.filter(queries)

    context = {
        'classes': classes,
        'search_term': query,
    }

    return render(request, 'classes/classes.html', context)


def class_detail(request, class_id):
    """ A view to show individual class details """

    a_class = get_object_or_404(Class, pk=class_id)

    context = {
        'class': a_class,
    }

    return render(request, 'classes/class_detail.html', context)
