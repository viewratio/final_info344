# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-20 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitSent', '0010_auto_20160819_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bad',
            field=models.CharField(default='', max_length=200),
        ),
    ]
