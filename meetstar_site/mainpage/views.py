from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


def index(request):
    return render(request, 'mainpage/base.html')

def carousel(request):
    return render(request, 'mainpage/carousel_partners.html')

def how_to(request):
    return render(request, 'mainpage/how_to.html')

def events(request):
    return render(request, 'mainpage/events.html')

def media(request):
     return render(request, 'mainpage/media.html')