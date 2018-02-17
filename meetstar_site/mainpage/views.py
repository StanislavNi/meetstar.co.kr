from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .models import Events
from django.contrib import auth
import datetime

import logging

logger = logging.getLogger(__name__)

def index(request):
    upcoming_events = Events.objects.filter(winner__isnull=True,
                                            date__gt=datetime.datetime.now())
    ctx = {'upcoming_events': upcoming_events, 'is_auth': request.user.is_authenticated}
    return render(request, 'mainpage/index.html', context=ctx)

def randomize(request):
    event_id = request.GET['event_id']
    try:
        event = Events.objects.get(id=event_id)
        event.randomize()
    except Events.DoesNotExist:
        return HttpResponse('Event with ID {0} doesnt exist'.format(event_id))

    return HttpResponse(event)

def account_page(request):
    ctx = {'user': request.user}
    return render(request, 'mainpage/account_page.html', context=ctx)

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/')
        else:
            login_error = 'User not exist'
            context = {'login_error': login_error}
            return render(request, 'login_auth/login.html', context)
    else:
        return render(request, 'login_auth/login.html', context)
