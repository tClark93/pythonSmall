from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^main$', views.main),
    url(r'^post$', views.post),
    url(r'^comment$', views.comment),
    url(r'^logoff$', views.logoff),
    # url(r'^(?P<id>\d+)/destroy$', views.destroy),
]