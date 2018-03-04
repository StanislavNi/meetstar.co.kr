from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^profile$', views.profile, name=''),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^password/$', views.password, name=''),
    url(r'^details_event$', views.details_event, name=''),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [ url(r'^accounts/', include('django.contrib.auth.urls')),]
