# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-28 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btblogers', '0017_auto_20160405_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brands',
            name='image',
            field=models.ImageField(blank=True, default=b'/Users/zannasapoval/djcode/blogers/media/brands/default_brands.jpg', null=True, upload_to='brands'),
        ),
        migrations.AlterField(
            model_name='products',
            name='foto',
            field=models.ImageField(blank=True, default=b'/Users/zannasapoval/djcode/blogers/media/products/default.jpg', null=True, upload_to='products'),
        ),
    ]
