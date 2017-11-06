from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import Tutorial, Ingredient, Step

def populate(request):

    bakedChicken = Tutorial.objects.create(name="Baked Chicken", duration=100)
    step1 = Step.objects.create(tutorial = bakedChicken, timestamp = 10, action = 'pause', stepNumber = 1, content = 'none', shortDesc = 'Marinate the chicken', longDesc = 'Marinate the chicken using all these new ingredients')
    step2 = Step.objects.create(tutorial = bakedChicken, timestamp = 20, action = 'timer', stepNumber = 2, content = '10', shortDesc = 'Put chicken in oven', longDesc = 'Place chicken in over for 10 minutes')
    step3 = Step.objects.create(tutorial = bakedChicken, timestamp = 30, action = 'timer', stepNumber = 3, content = '15', shortDesc = 'Turn chicken over', longDesc = 'Turn the chicken over for another 15 minutes until cooked')
    step4 = Step.objects.create(tutorial = bakedChicken, timestamp = 40, action = 'play', stepNumber = 4, content = 'none', shortDesc = 'Let rest', longDesc = 'Let the food rest')

    bakedChicken.steps.add(step1)
    bakedChicken.steps.add(step2)
    bakedChicken.steps.add(step3)
    bakedChicken.steps.add(step4)

    bakedChicken.save()

    return HttpResponse('woohoo')


    print "hit populate"
