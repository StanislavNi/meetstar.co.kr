from django.contrib import admin
from .models import Events
from .models import UsersInEvent

admin.site.register(Events)
admin.site.register(UsersInEvent)
