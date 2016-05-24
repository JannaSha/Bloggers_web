# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 17:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btblogers', '0002_auto_20160331_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discriptionblogers',
            name='age',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='discriptionblogers',
            name='city',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='discriptionblogers',
            name='country',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='discriptionblogers',
            name='foto',
            field=models.ImageField(blank=True, upload_to='blogers'),
        ),
        migrations.AlterField(
            model_name='discriptionblogers',
            name='sur_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='discriptionblogers',
            name='url_instagramm',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='color',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='type_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='btblogers.Types'),
        ),
    ]
