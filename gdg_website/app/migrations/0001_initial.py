# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=120)),
                ('date_from', models.DateTimeField(auto_now=True)),
                ('date_to', models.DateTimeField(auto_now=True)),
                ('venue', models.CharField(max_length=120)),
                ('speaker', models.CharField(max_length=120)),
                ('event_type', models.CharField(max_length=120)),
                ('registration_link', models.URLField(max_length=120)),
                ('facebook_link', models.URLField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/Event')),
                ('description', models.TextField()),
                ('contact', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/Project')),
                ('description', models.TextField()),
                ('host_link', models.URLField(max_length=120)),
                ('github_link', models.URLField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_ID', models.EmailField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=120)),
                ('status', models.CharField(max_length=120)),
                ('email_ID', models.EmailField(max_length=200)),
                ('facebook_link', models.URLField(max_length=120)),
                ('github_link', models.URLField(max_length=120)),
                ('twitter_link', models.URLField(max_length=120)),
                ('linkedin_link', models.URLField(max_length=120)),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/Team')),
                ('position', models.CharField(max_length=120)),
            ],
        ),
    ]