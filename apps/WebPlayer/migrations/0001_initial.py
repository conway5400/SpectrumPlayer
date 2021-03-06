# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 05:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=255)),
                ('lastRequest', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('command', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpectrumBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('macAddress', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('lastOnline', models.DateTimeField(null=True)),
                ('ipAddress', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.IntegerField()),
                ('action', models.CharField(max_length=100)),
                ('stepNumber', models.IntegerField()),
                ('content', models.CharField(max_length=255)),
                ('shortDesc', models.CharField(max_length=255)),
                ('longDesc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='step',
            name='tutorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='WebPlayer.Tutorial'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='tutorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='WebPlayer.Tutorial'),
        ),
    ]
