from django.shortcuts import render, redirect
from mainpage.models import UsersInEvent
from . import forms

def profile(request):
    user_events = []
    if request.user.is_authenticated:
        user_events = UsersInEvent.objects.filter(user=request.user)
    if request.method == 'POST':
        form = forms.UserForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            print(1111)
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            return redirect('')
        else:
            print(222)
    form = forms.UserForm(data=request.POST)
    ctx = {'user': request.user, 'user_events': user_events, 'form': form}
    return render(request, 'userprofile/account_page.html', context=ctx,)
