from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Events, UsersInEvent
from content.models import Videos
from django.contrib import auth
import datetime

import logging

logger = logging.getLogger(__name__)

def index(request):
    upcoming_events = Events.objects.filter(winner__isnull=True,
                                            date__gt=datetime.datetime.now())
    user_events = []

    if request.user.is_authenticated:
        user_events = UsersInEvent.objects.filter(user=request.user)
        event_ids = user_events.values_list('event_id', flat=True)
    else:
        event_ids = None
    videos = Videos.objects.filter(address__isnull=False)
    ctx = {
        'user_event_ids': event_ids,
        'upcoming_events': upcoming_events,
        'user': request.user,
        'user_events': user_events,
        'videos': videos,
    }
    return render(request, 'mainpage/index.html', context=ctx)

def randomize(request):
    event_id = request.GET['event_id']
    try:
        event = Events.objects.get(id=event_id)
        event.randomize()
    except Events.DoesNotExist:
        return HttpResponse('Event with ID {0} doesnt exist'.format(event_id))

    return HttpResponse(event)

def login(request):
    context = {'user': request.user}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/profile')
        else:
            login_error = 'User not exist'
            context = {'login_error': login_error}
            return render(request, 'mainpage/login.html', context)
    else:
        return render(request, 'mainpage/login.html', context)

def participate(request):
    event_add = UsersInEvent.objects.get_or_create(user=request.user,
                                            event_id=request.GET['event_id'])
    return redirect('/events')

def events(request):
    user_events = []
    upcoming_events = Events.objects.filter(winner__isnull=True,
                                            date__gt=datetime.datetime.now())
    past_events = Events.objects.filter(date__lt=datetime.datetime.now())
    if request.user.is_authenticated:
        user_events = UsersInEvent.objects.filter(user=request.user)
        event_ids = user_events.values_list('event_id', flat=True)
    ctx = {
        'user_event_ids': event_ids,
        'upcoming_events': upcoming_events,
        'user': request.user,
        'user_events': user_events,
        'past_events': past_events,
    }
    return render(request, 'mainpage/events_page.html', ctx)

def paywall(request):
    event = Events.objects.get(id=request.GET['event_id'])
    return render(request, 'mainpage/paywall.html', {'event': event})


def details_event(request):
    event = Events.objects.get(id=request.GET['event_id'])
    return render(request, 'mainpage/details_event.html', {'event': event})
