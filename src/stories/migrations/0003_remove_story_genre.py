# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 23:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_story_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='genre',
        ),
    ]
