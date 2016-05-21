# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-05 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btblogers', '0011_auto_20160401_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='html_video',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='brands',
            name='image',
            field=models.ImageField(blank=True, default=b'/Users/zannasapoval/djcode/Web_blogres/blogers/media/brands/default_brands.jpg', null=True, upload_to='brands'),
        ),
        migrations.AlterField(
            model_name='products',
            name='foto',
            field=models.ImageField(blank=True, default=b'/Users/zannasapoval/djcode/Web_blogres/blogers/media/products/default.jpg', null=True, upload_to='products'),
        ),
    ]
