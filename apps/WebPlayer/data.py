from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import Tutorial, Ingredient, Step, Action

def populate(request):

    beefTenderloin = Tutorial.objects.create(name = "Beef Tenderloin", duration = 220, video = "https://d34j7w7zsvll58.cloudfront.net/media/655894_bde292f2d4137c0f0abb8b611622b976/655894.mpd")

    step1 = Step.objects.create(startTime = 0, stepNumber = 1, shortDesc = "Marinate the steak", longDesc = "Place the beef tenderloin flat on a cutting board. Liberally season all sides of the meat with salt and pepper.", tutorial = beefTenderloin)

    step2 = Step.objects.create(startTime = 33, stepNumber = 2, shortDesc = "Pre-heat peanut oil in pan", longDesc = "Add oil to a hot pan. Peanut oil is a great option. Wait for the oil to begin smoking before moving on.", tutorial = beefTenderloin)

    step3 = Step.objects.create(startTime = 52, stepNumber = 3, shortDesc = "Cook the meat on both sides", longDesc = "Add the meat when the oil begins to smoke. Sear both sides of the meat until a golden brown crust forms. About 2-3 minutes per side. Move on when you have seared both sides.", tutorial = beefTenderloin)

    step4 = Step.objects.create(startTime = 72, stepNumber = 4, shortDesc = "Add butter, garlic, thyme, and rosemary", longDesc = "Once seared on both sides, add butter and lower the heat so it doesn't burn. Add 2-3 cloves of garlic. Add fresh thyme and rosemary. Continue to baste the meat with the butter.", tutorial = beefTenderloin)

    step5 = Step.objects.create(startTime = 148, stepNumber = 5, shortDesc = "Let meat rest for 2 minutes", longDesc = "Let the meat rest for roughly 2 minutes", tutorial = beefTenderloin)

    step6 = Step.objects.create(startTime = 159, stepNumber = 6, shortDesc = "Slice & garnish meat for serving!", longDesc = "Remove string from meat and slice meat diagonally. Add meat to plate for serving. Top with sea salt, olive oil, and herbs leftover from the pan.", tutorial = beefTenderloin)

    action1 = Action.objects.create(timestamp = 33, action = "pause", tutorial = beefTenderloin)
    action2 = Action.objects.create(timestamp = 52, action = "pause", tutorial = beefTenderloin)
    action3 = Action.objects.create(timestamp = 53, action = "timer", content = "180", tutorial = beefTenderloin)
    action3 = Action.objects.create(timestamp = 15, action = "timer", content = "180", tutorial = beefTenderloin)
    action4 = Action.objects.create(timestamp = 72, action = "pause", tutorial = beefTenderloin)
    action5 = Action.objects.create(timestamp = 102, action = "tip", content = "Remember to keep basting the beef with butter!", tutorial = beefTenderloin)
    action5 = Action.objects.create(timestamp = 10, action = "tip", content = "Leave in fridge overnight for better flavoring!", tutorial = beefTenderloin)
    action6 = Action.objects.create(timestamp = 157, action = "timer", content = "120", tutorial = beefTenderloin)
    action7 = Action.objects.create(timestamp = 158, action = "pause", tutorial = beefTenderloin)

    Ingredient.objects.create(name = 'Beef tenderloin', descr = '8 ounce filet', tutorial = beefTenderloin)
    Ingredient.objects.create(name = 'Peanut oil', descr = '2 tablespoons', tutorial = beefTenderloin)

    Ingredient.objects.create(name = 'Butter', descr = '1/2 Cup', tutorial = beefTenderloin)
    Ingredient.objects.create(name = 'Garlic', descr = '3 Cloves, Peeled', tutorial = beefTenderloin)
    Ingredient.objects.create(name = 'Fresh Thyme', descr = '3 Sprigs', tutorial = beefTenderloin)
    Ingredient.objects.create(name = 'Fresh Rosemary', descr = '3 Sprigs', tutorial = beefTenderloin)
    Ingredient.objects.create(name = 'Sea Salt', descr = 'to taste', tutorial = beefTenderloin)
    Ingredient.objects.create(name = 'Ground Pepper', descr = 'taste', tutorial = beefTenderloin)


    return HttpResponse('woohoo')


    print "hit populate"
