from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
import django.contrib.auth.views as auth_views

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^profile$', views.profile, name=''),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [ url(r'^accounts/', include('django.contrib.auth.urls')),]
