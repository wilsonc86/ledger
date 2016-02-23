# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 05:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addressbook', '0002_auto_20160204_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_to', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('organisation_name', models.CharField(blank=True, max_length=256, null=True)),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wildlife_licence_customerrole_created', to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wildlife_licence_customerrole_modified', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WildlifeLicence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_to', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('submitted', 'Submitted'), ('granted', 'Granted'), ('refused', 'Refused'), ('cancelled', 'Cancelled'), ('expired', 'Expired')], default='submitted', max_length=64)),
                ('licence_no', models.CharField(blank=True, max_length=64, null=True, unique=True)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('expire_date', models.DateField(blank=True, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='addressbook.Address')),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wildlife_licence_wildlifelicence_created', to=settings.AUTH_USER_MODEL)),
                ('customer_role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wildlife_licence.CustomerRole')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WildlifeLicenceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_to', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
                ('code', models.CharField(blank=True, max_length=64)),
                ('description', models.TextField(blank=True)),
                ('creator', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wildlife_licence_wildlifelicencetype_created', to=settings.AUTH_USER_MODEL)),
                ('modifier', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wildlife_licence_wildlifelicencetype_modified', to=settings.AUTH_USER_MODEL)),
                ('replaced_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wildlife_licence.WildlifeLicenceType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='wildlifelicence',
            name='licence_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wildlife_licence.WildlifeLicenceType'),
        ),
        migrations.AddField(
            model_name='wildlifelicence',
            name='modifier',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wildlife_licence_wildlifelicence_modified', to=settings.AUTH_USER_MODEL),
        ),
    ]
