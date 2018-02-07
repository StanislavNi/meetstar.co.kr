from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True)
    photo = models.ImageField(null=True)

    def randomize(self):
        print(self.userinevent_set.all().values('user'))



class UsersInEvent(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Events)

    class Meta:
        unique_together = ('user', 'event')
