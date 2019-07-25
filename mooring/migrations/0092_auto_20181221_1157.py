# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-12-21 03:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mooring', '0091_delete_uniqueseqid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChangeGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='RefundPricePeriod',
            new_name='ChangePricePeriod',
        ),
        migrations.RemoveField(
            model_name='refundgroup',
            name='refund_period',
        ),
        migrations.RemoveField(
            model_name='bookingperiodoption',
            name='refund_group',
        ),
        migrations.DeleteModel(
            name='RefundGroup',
        ),
        migrations.AddField(
            model_name='changegroup',
            name='change_period',
            field=models.ManyToManyField(related_name='refund_period_options', to='mooring.ChangePricePeriod'),
        ),
        migrations.AddField(
            model_name='bookingperiodoption',
            name='change_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mooring.ChangeGroup'),
        ),
    ]
