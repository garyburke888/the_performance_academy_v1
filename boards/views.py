from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def boards(request):
    return HttpResponse('Hello, World!')
