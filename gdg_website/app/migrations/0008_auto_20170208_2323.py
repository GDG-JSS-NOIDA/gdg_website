# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 17:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170208_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='event_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Event'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='comment_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Comment'),
        ),
    ]
