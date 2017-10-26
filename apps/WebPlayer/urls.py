from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^alexa$', views.alexa),
    url(r'^health$', views.health),
]
