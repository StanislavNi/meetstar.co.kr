from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'', views.index, name='index'),
    url(r'', views.carousel, name='carousel'),
    url(r'', views.how_to, name='how_to'),
    url(r'', views.events, name='events'),
    url(r'', views.media, name='media'),
]
