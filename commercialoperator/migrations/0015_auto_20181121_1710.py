# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-21 09:10
from __future__ import unicode_literals

import commercialoperator.components.compliances.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0014_auto_20181121_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200)),
                ('visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(upload_to=commercialoperator.components.compliances.models.update_proposal_complaince_filename),
        ),
    ]
