# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-04 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingrange',
            name='campground',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='booking_ranges', to='parkstay.Campground'),
        ),
        migrations.AlterField(
            model_name='bookingrange',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campsite',
            name='campground',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='campsites', to='parkstay.Campground'),
        ),
    ]
