# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btblogers', '0006_auto_20160331_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='additional_info',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='type_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='btblogers.Types'),
        ),
        migrations.AlterField(
            model_name='products',
            name='url',
            field=models.URLField(blank=True, default=None, null=True),
        ),
    ]