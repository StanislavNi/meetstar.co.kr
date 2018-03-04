from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mainpage.models import UsersInEvent, Events
from . import forms
from .forms import UserCreateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def profile(request):
    user_events = []
    if request.user.is_authenticated:
        user_events = UsersInEvent.objects.filter(user=request.user)

    if request.method == 'POST':
        form = forms.UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = forms.UserForm(instance=request.user)

    ctx = {'user': request.user, 'user_events': user_events, 'form': form}
    return render(request, 'userprofile/account_page.html', context=ctx,)

def signup(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            print(username,raw_password)
            login(request, user)
            return redirect('')
    else:
        form = UserCreateForm()
    return render(request, 'userprofile/signup.html', {'form': form})

def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'userprofile/password_change.html', {
        'form': form
    })

def details_event(request):
    event = Events.objects.get(id=request.GET['event_id'])
    return render(request, 'userprofile/details_event.html', {'event': event})
