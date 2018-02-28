from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
import django.contrib.auth.views as auth_views

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^randomize$', views.randomize, name=''),
    url(r'^login/$', views.login, name ='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'},
        name='logout'),
    url(r'^participate$', views.participate, name=''),
    url(r'^events$', views.events, name=''),
    url(r'^paywall$', views.paywall, name=''),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [ url(r'^accounts/', include('django.contrib.auth.urls')),]
