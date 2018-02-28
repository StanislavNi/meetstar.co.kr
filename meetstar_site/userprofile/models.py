from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Profile(AbstractUser):
    bio = models.TextField(verbose_name=_('bio'), blank=True)
    avatar = models.ImageField(upload_to='avatars', verbose_name=_('avatar'), blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'profiles'
        verbose_name = _('user profile')
        verbose_name_plural = _('user profiles')
