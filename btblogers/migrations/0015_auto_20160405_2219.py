# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btblogers', '0014_remove_video_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='html_video',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
