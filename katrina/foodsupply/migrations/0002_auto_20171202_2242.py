# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodsupply', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='household',
            name='hub',
        ),
        migrations.AddField(
            model_name='household',
            name='household_id',
            field=models.IntegerField(default=0),
        ),
    ]
