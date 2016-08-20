# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-19 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitSent', '0002_remove_post_sentiment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sent',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='tweetContent',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]