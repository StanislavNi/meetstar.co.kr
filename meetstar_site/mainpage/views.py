import datetime
import logging

from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.template import loader

from content.models import Videos
from .models import Events, UsersInEvent
from userprofile.models import Profile
from meetstar_site import settings


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
        winner_id = event.randomize()
    except Events.DoesNotExist:
        return HttpResponse('Event with ID {0} doesnt exist'.format(event_id))
    all_event_users = UsersInEvent.objects.filter(event_id=event_id)
    winner_user = Profile.objects.get(id=winner_id)
    for user_in_event in all_event_users:
        html_message = loader.render_to_string(
            'mainpage/mail.htm',
            {
                'username': user_in_event.user,
                'winner_user': winner_user,
            })
        send_mail('It is time for event', '',
                  settings.EMAIL_HOST_USER, [user_in_event.user.email],
                  fail_silently=False, html_message=html_message)
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
    return redirect('events')

def events(request):
    user_events = []
    upcoming_events = Events.objects.filter(winner__isnull=True,
                                            date__gt=datetime.datetime.now())
    past_events = Events.objects.filter(date__lt=datetime.datetime.now())
    if request.user.is_authenticated:
        user_events = UsersInEvent.objects.filter(user=request.user)
        event_ids = user_events.values_list('event_id', flat=True)
    else:
        event_ids = None
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
    users_in_event = UsersInEvent.objects.filter(event=event)
    return render(request, 'mainpage/details_event.html',
                  {'event': event, 'users_in_event': users_in_event})
