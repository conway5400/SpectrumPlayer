# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.http import JsonResponse
from ..WebPlayer.models import Tutorial

import json

# Create your views here.

def getTutorial(request, id):
    # print Tutorial.objects.get(id = id).values()
    try:
        tutorialResults = Tutorial.objects.filter(id = id)
        tutorial = tutorialResults[0]
        steps = tutorial.steps.all().order_by("stepNumber")

        tutorialJson = serializers.serialize("json", tutorialResults)
        stepsJson = serializers.serialize("json", steps)

        jsonResponse = '{ "tutorial" : ' + tutorialJson + ', "steps" : ' + stepsJson +'}'
        
        return HttpResponse(jsonResponse)
    except:
        print "Couldn't find Tutorial!"
        return HttpResponse('error')


def getAllTutorials(request):

    allTutorials_json = serializers.serialize("json", Tutorial.objects.all())

    return HttpResponse(serializers.serialize("json", Tutorial.objects.all()))
