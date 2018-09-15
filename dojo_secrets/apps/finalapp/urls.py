from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^main$', views.main),
    url(r'^share$', views.share),
    url(r'^like$', views.like),
    url(r'^top$', views.top),
    url(r'^logout', views.logout),
    ]