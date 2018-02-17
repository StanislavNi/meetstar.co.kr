from django.shortcuts import render
from django.http import HttpResponse
from .models import Events
from django.contrib.auth.models import User
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


def upcoming(request):
    up_events = request.GET.get['event']
    return HttpResponse(up_events)

def account_page(request):
    ctx = {'user': request.user}
    return render(request, 'mainpage/account_page.html', context=ctx)
