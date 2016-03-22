# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-13 14:04
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='state',
            field=models.CharField(choices=[('draft', 'Draft'), ('lodged', 'Lodged')], default='draft', max_length=20, verbose_name='Application State'),
            preserve_default=False,
        ),
    ]