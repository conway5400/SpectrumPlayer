# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from alexa import monthsFromServer
from models import Request

# Create your views here.
def index(request):
    return render(request, 'WebPlayer/index.html')

@csrf_exempt
def alexa(request):
    print 'woooohhooooo'
    return HttpResponse({'response' : 'test'})

def health(request):
    return HttpResponse(status = 200)

def updates(request):
    userCommands = Request.objects.order_by('-createdAt')
    if userCommands:
        lastCommand = userCommands[0].command
        userCommands.delete()
        return HttpResponse(lastCommand)
    else:
        return HttpResponse(None)

def showAlexa(request):
    print monthsFromServer
    context = {
        'months' : monthsFromServer
    }
    return render(request, 'WebPlayer/alexa.html', context)


