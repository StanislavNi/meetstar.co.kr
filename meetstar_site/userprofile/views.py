from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from mainpage.models import UsersInEvent
from . import forms

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
        #create form and meta
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'userprofile/signup.html', {'form': form})
