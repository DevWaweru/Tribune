# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180605_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='/static/Images/lambo.jpg', upload_to='articles/'),
        ),
    ]
