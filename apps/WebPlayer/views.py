# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import json

from models import Request, SpectrumBox, Tutorial
import time

from urllib2 import urlopen, unquote
from urlparse import parse_qs, urlparse

import requests


# Create your views here.
def index(request):
    return render(request, 'WebPlayer/index.html')

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

def boxStatus(request):
    url = "http://spectrumbox.ngrok.io"
    statusCode = urlopen(url).getcode()
    if(statusCode == 200):
        return HttpResponse('Box is online!')
    else:
        return HttpResponse('Couldnt find box...')

@csrf_exempt
def newBoxOnline(request):
    print "there's a new box online....!"
    bodyReq = unquote(request.body)
    query = parse_qs(bodyReq)
    macAddress = query['macAddress'][0]

    results = SpectrumBox.objects.getBox(macAddress)

    print "Box Result Found || Last Online: {} || MAC: {}".format(results.lastOnline, results.macAddress)
    
    return HttpResponse('thanks for letting me know!')

def tutorials(request):
    context = {
        'tutorials' : Tutorial.objects.all()
    }
    return render(request, 'WebPlayer/tutorials.html', context)


def cooking(request, id):
    context = {
        'results' : Tutorial.objects.get(id = id)
    }
    return render(request, 'WebPlayer/cooking.html', context)
