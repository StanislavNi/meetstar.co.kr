from django.shortcuts import render
from django.http import HttpResponse
from .models import Events
import datetime

import logging

logger = logging.getLogger(__name__)

def index(request):
    upcoming_events = Events.objects.filter(winner__isnull=True,
                                            date__gt=datetime.datetime.now())
    ctx = {'upcoming_events': upcoming_events}
    return render(request, 'mainpage/index.html', context=ctx)


def randomize(request):
    event_id = request.GET['event_id']
    try:
        event = Events.objects.get(id=event_id)
        event.randomize()
    except Events.DoesNotExist:
        return HttpResponse('Event with ID {0} doesnt exist'.format(event_id))

    return HttpResponse(event)
