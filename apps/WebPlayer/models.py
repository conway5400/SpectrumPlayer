# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Request(models.Model):
    command = models.CharField(max_length = 100)
    createdAt = models.DateTimeField(auto_now_add= True)

# Create your models here.
