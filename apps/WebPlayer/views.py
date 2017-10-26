# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'WebPlayer/index.html')

def alexa(request):
    print 'woooohhooooo'
    return HttpResponse('Alexa works!')

def health(request):
    return HttpResponse(status = 200)
