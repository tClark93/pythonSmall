from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<id>\d+)/remove$', views.remove),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)/destroy$', views.destroy),
]