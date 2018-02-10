from django.db import models
from django.contrib.auth.models import User
import random
import datetime


class Events(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    winner = models.ForeignKey(User, null=True, blank=True)
    detail = models.TextField(null=True)
    photo = models.ImageField(null=True, blank=True)

    def randomize(self):
        print('----- starting randomize')

        users_list = self.usersinevent_set.all().values_list('user', flat=True)

        self.winner_id = random.choice(users_list)

        self.save()

    def upcoming(self):
        up_events = Events.objects.filter(date__gt=datetime.datetime.now)
        return up_events

    def __str__(self):
        return 'Event: {0}'.format(self.title)


class UsersInEvent(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Events)

    def __str__(self):
        return 'UsersInEvent: {0}, {1}'.format(self.event.title, self.user)

    class Meta:
        unique_together = ('user', 'event')
