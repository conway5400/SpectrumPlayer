# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 06:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebPlayer', '0002_auto_20171108_0207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='qty',
            new_name='descr',
        ),
    ]