from django.conf.urls import url
from django.contrib import admin
from . import views
from . import alexa

urlpatterns = [
    url(r'^$', views.index),
    url(r'^alexa$', views.alexa),
    url(r'^showAlexa$', views.showAlexa),
    url(r'^health$', views.health),
    url(r'^alexaBeta$', alexa.incomingRoute),
]
