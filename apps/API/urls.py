from django.conf.urls import url
from django.contrib import admin
from . import api

urlpatterns = [
    url(r'^tutorials/(?P<id>\d+)/$', api.getTutorial),
    url(r'^tutorials/$', api.getAllTutorials),

]
