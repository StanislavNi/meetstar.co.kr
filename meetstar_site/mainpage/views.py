from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Events

import logging

logger = logging.getLogger(__name__)



def index(request):
    # upcoming_events = ...

    # cntx = {'upcoming_events': upcoming_events}

    return render(request, 'mainpage/index.html', )

def randomize(request):
    event_id = request.GET['event_id']
    try:
        event = Events.objects.get(id=event_id)
    except Events.DoesNotExist:
        return HttpResponse('Event with ID {0} doesnt exist'.format(event_id))

    return HttpResponse(event)

def upcoming(request):
    up_events = request.GET.get['event']
    return HttpResponse(up_events)
