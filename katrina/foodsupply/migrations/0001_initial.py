# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 17:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='household',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_population', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('hub_id', models.AutoField(primary_key=True, serialize=False)),
                ('population', models.IntegerField(default=0)),
                ('current_storage', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='household',
            name='hub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodsupply.Hub'),
        ),
    ]
