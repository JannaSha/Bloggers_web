# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btblogers', '0005_auto_20160331_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
