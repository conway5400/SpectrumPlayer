from django.conf.urls import url
from django.contrib import admin
from . import views
from . import alexa
from . import data

urlpatterns = [
    url(r'^$', views.index),
    url(r'^cooking/(?P<id>\d+)/$', views.cooking),
    url(r'^health$', views.health),
    url(r'^updates$', views.updates),
    url(r'^boxStatus$', views.boxStatus),
    url(r'^newBoxOnline$', views.newBoxOnline),
    url(r'^alexaBeta$', alexa.incomingRoute),
    url(r'^populateData$', data.populate),
    url(r'^tutorials$', views.tutorials)
]
