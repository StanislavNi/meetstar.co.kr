from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^randomize$', views.randomize, name=''),
    url(r'^account_page$', views.account_page, name=''),
    url(r'^login/$', views.login, name ='login'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [ url(r'^accounts/', include('django.contrib.auth.urls')),]
