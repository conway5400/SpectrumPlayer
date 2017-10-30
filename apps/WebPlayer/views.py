# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from alexa import monthsFromServer

colors = ['red', 'blue', 'green']

# Create your views here.
def index(request):
    return render(request, 'WebPlayer/index.html')

@csrf_exempt
def alexa(request):
    print 'woooohhooooo'
    return HttpResponse({'response' : 'test'})

def health(request):
    return HttpResponse(status = 200)

def showAlexa(request):
    print monthsFromServer
    context = {
        'months' : monthsFromServer
    }
    return render(request, 'WebPlayer/alexa.html', context)


