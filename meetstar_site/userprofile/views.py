from django.shortcuts import render, redirect
from mainpage.models import UsersInEvent
from . import forms

def profile(request):
    user_events = []
    if request.user.is_authenticated:
        user_events = UsersInEvent.objects.filter(user=request.user)
    if request.method == 'POST':
        form = forms.UserForm(data=request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('')
    form = forms.UserForm(data=request.POST)
    ctx = {'user': request.user, 'user_events': user_events, 'form': form}
    return render(request, 'userprofile/account_page.html', context=ctx,)
