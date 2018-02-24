from django.shortcuts import render
from mainpage.models import UsersInEvent

def profile(request):
    user_events = []
    if request.user.is_authenticated:
        user_events = UsersInEvent.objects.filter(user=request.user)
    ctx = {'user': request.user, 'user_events': user_events}
    return render(request, 'userprofile/account_page.html', context=ctx,)
