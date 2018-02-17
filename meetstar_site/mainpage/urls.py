from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^randomize$', views.randomize, name=''),
    url(r'^upcoming$', views.upcoming, name=''),
    url(r'^account_page$', views.account_page, name=''),
]
