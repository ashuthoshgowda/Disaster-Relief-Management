# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 22:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodsupply', '0002_auto_20171202_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='hub_id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]
