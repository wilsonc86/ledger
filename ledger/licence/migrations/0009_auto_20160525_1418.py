# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-25 06:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licence', '0008_auto_20160524_0924'),
    ]

    operations = [
        migrations.RenameField(
            model_name='licence',
            old_name='user',
            new_name='holder',
        ),
    ]
