# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-01 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0042_wildlifelicenceactivitytype_schema'),
    ]

    operations = [
        migrations.AddField(
            model_name='wildlifelicenceactivitytype',
            name='licence_activity_status',
            field=models.CharField(choices=[('current', 'Current'), ('expired', 'Expired'), ('cancelled', 'Cancelled'), ('surrendered', 'Surrendered'), ('suspended', 'Suspended')], default='current', max_length=40),
        ),
    ]
