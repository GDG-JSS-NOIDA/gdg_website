# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170205_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_ID', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=120)),
                ('email_ID', models.EmailField(max_length=120)),
                ('date', models.DateTimeField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_ID', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=120)),
                ('email_ID', models.EmailField(max_length=120)),
                ('date', models.DateTimeField()),
                ('comment', models.TextField()),
            ],
        ),
    ]
