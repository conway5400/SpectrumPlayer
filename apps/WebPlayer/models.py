# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import time

class UserManager(models.Manager):
    def getUser(self, id):
        checkUser = self.filter(userId = id)
        if len(checkUser) <= 0:
            return User.objects.create(userId = id)
        else:
            return checkUser[0]


class SpectrumBoxManager(models.Manager):
    #get box and create if doesnt exist
    def getBox(self, macAddress):
        box = self.filter(macAddress = macAddress)

        if(len(box) == 0):
            print "New Box, creating record..." 
            return self.createBox(macAddress)
        else:
            box = box[0]
            #set last online time
            self.setLastOnline(box)
            print "Box previously registered..."
            return box

    def createBox(self, macAddress):
        macAddress = macAddress.replace(" ", "")
        newBox = SpectrumBox.objects.create(macAddress = macAddress)
        self.setLastOnline(newBox)
        return newBox

    def setLastOnline(self, box):
        box.lastOnline = time.strftime("%Y-%m-%dT%H:%M:%S+0000")
        box.save()
        return self
        # print "setting last online to right now! {}".format(time.strftime("%Y-%m-%dT%H:%M:%S+0000"))

class SpectrumBox(models.Model):
    macAddress = models.CharField(max_length = 255)
    createdAt = models.DateTimeField(auto_now_add = True)
    lastOnline = models.DateTimeField(null = True)
    ipAddress = models.CharField(max_length = 255)
    objects = SpectrumBoxManager()

class AmazonUser(models.Model):
    userId = models.CharField(max_length = 255)
    lastRequest = models.DateTimeField()

class User(models.Model):
    userId = models.CharField(max_length = 255)
    objects = UserManager()
    # spectrumBox = models.OneToOneField(SpectrumBox)
    # amazonUser = models.OneToOneField(AmazonUser)

class Request(models.Model):
    command = models.CharField(max_length = 100)
    createdAt = models.DateTimeField(auto_now_add= True)
    # user = models.ForeignKey(User, related_name = 'requests')

        
class Tutorial(models.Model):
    name = models.CharField(max_length = 100)
    video = models.CharField(max_length=255)
    duration = models.IntegerField()

class Action(models.Model):
    tutorial = models.ForeignKey(Tutorial, related_name = 'actions')
    timestamp = models.IntegerField()
    action = models.CharField(max_length = 100)
    content = models.CharField(max_length = 255)

class Step(models.Model):
    tutorial = models.ForeignKey(Tutorial, related_name = 'steps')
    startTime = models.IntegerField()
    stepNumber = models.IntegerField()
    shortDesc = models.CharField(max_length = 255)
    longDesc = models.CharField(max_length = 255)

class Ingredient(models.Model):
    step = models.ForeignKey(Step, related_name = 'ingredients', blank=True, null=True)
    name = models.CharField(max_length = 255)
    descr = models.CharField(max_length = 255)
    tutorial = models.ForeignKey(Tutorial, related_name = 'ingredients')
