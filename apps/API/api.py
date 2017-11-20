# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
from django.http import JsonResponse
from ..WebPlayer.models import Tutorial

import json

# Create your views here.

def deleteTutorial(request, id):
    Tutorial.objects.get(id = id).delete()
    return redirect('/tutorials')

def getTutorial(request, id):
    # print Tutorial.objects.get(id = id).values()
    try:
        tutorialResults = Tutorial.objects.filter(id = id)
        tutorial = tutorialResults[0]
        steps = tutorial.steps.all().order_by("stepNumber")
        actions = tutorial.actions.all().order_by("timestamp")
        ingredients = tutorial.ingredients.all()

        tutorialJson = serializers.serialize("json", tutorialResults)
        stepsJson = serializers.serialize("json", steps)
        actionsJson = serializers.serialize("json", actions)
        ingredients = serializers.serialize("json", ingredients)

        jsonResponse = '{ "tutorial" : ' + tutorialJson + ', "steps" : ' + stepsJson + ', "actions" : ' + actionsJson + ', "ingredients" : ' + ingredients + '}'
        
        return HttpResponse(jsonResponse)
    except:
        print "Couldn't find Tutorial!"
        return HttpResponse('error')



def getAllTutorials(request):

    allTutorials_json = serializers.serialize("json", Tutorial.objects.all())

    return HttpResponse(serializers.serialize("json", Tutorial.objects.all()))
